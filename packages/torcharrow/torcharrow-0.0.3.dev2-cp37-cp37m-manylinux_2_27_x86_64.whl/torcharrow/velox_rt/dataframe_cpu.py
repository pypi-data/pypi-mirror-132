#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
from __future__ import annotations

import array as ar
import functools
from abc import abstractmethod
from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
    Iterable,
    Iterator,
    OrderedDict,
)

import numpy as np
import torcharrow as ta
import torcharrow._torcharrow as velox
import torcharrow.dtypes as dt
import torcharrow.pytorch as pytorch
from tabulate import tabulate
from torcharrow.dispatcher import Dispatcher
from torcharrow.expression import eval_expression, expression
from torcharrow.icolumn import IColumn
from torcharrow.idataframe import IDataFrame
from torcharrow.scope import Scope
from torcharrow.trace import trace, traceproperty

from .column import ColumnFromVelox
from .typing import get_velox_type

# assumes that these have been imported already:
# from .inumerical_column import INumericalColumn
# from .istring_column import IStringColumn
# from .imap_column import IMapColumn
# from .ilist_column import IListColumn

# ------------------------------------------------------------------------------
# DataFrame Factory with default scope and device


# -----------------------------------------------------------------------------
# DataFrames aka (StructColumns, can be nested as StructColumns:-)

DataOrDTypeOrNone = Optional[Union[Mapping, Sequence, dt.DType]]


class DataFrameCpu(ColumnFromVelox, IDataFrame):
    """Dataframe, ordered dict of typed columns of the same length"""

    def __init__(self, device: str, dtype: dt.Struct, data: Dict[str, ColumnFromVelox]):
        assert dt.is_struct(dtype)
        IDataFrame.__init__(self, device, dtype)

        self._data = velox.Column(get_velox_type(dtype))
        assert isinstance(data, dict)
        first = True
        for key, value in data.items():
            assert isinstance(value, ColumnFromVelox)
            assert first or len(value) == len(self._data)
            first = False
            # TODO: using a dict for field type lookup
            (field_dtype,) = (f.dtype for f in self.dtype.fields if f.name == key)

            col = value
            idx = self._data.type().get_child_idx(key)
            self._data.set_child(idx, col._data)
            self._data.set_length(len(col))
        self._finialized = False

    @property
    def _mask(self) -> List[bool]:
        return [self._getmask(i) for i in range(len(self))]

    # Any _full requires no further type changes..
    @staticmethod
    def _full(
        device: str,
        data: Dict[str, ColumnFromVelox],
        dtype: Optional[dt.Struct] = None,
        mask=None,
    ):
        assert mask is None  # TODO: remove mask parameter in _FullColumn
        cols = data.values()  # TODO: also allow data to be a single Velox RowColumn
        assert all(isinstance(c, ColumnFromVelox) for c in data.values())
        ct = 0
        if len(data) > 0:
            ct = len(list(cols)[0])
            if not all(len(c) == ct for c in cols):
                ValueError(f"length of all columns must be the same (e.g {ct})")
        inferred_dtype = dt.Struct([dt.Field(n, c.dtype) for n, c in data.items()])
        if dtype is None:
            dtype = inferred_dtype
        else:
            # TODO this must be weakened (to deal with nulls, etc)...
            if dtype != inferred_dtype:
                pass
                # raise TypeError(f'type of data {inferred_dtype} and given type {dtype} must be the same')
        return DataFrameCpu(device, dtype, data)

    # Any _empty must be followed by a _finalize; no other ops are allowed during this time

    @staticmethod
    def _empty(device: str, dtype: dt.Struct):
        field_data = {f.name: Scope._EmptyColumn(f.dtype, device) for f in dtype.fields}
        return DataFrameCpu(device, dtype, field_data)

    @staticmethod
    def _fromlist(device: str, data: List, dtype: dt.Struct):
        # default (ineffincient) implementation
        col = DataFrameCpu._empty(device, dtype)
        for i in data:
            col._append(i)
        return col._finalize()

    def _append_null(self):
        if self._finialized:
            raise AttributeError("It is already finialized.")
        df = self.append([None])
        self._data = df._data

    def _append_value(self, value):
        if self._finialized:
            raise AttributeError("It is already finialized.")
        df = self.append([value])
        self._data = df._data

    def _finalize(self):
        self._finialized = True
        return self

    def _fromdata(
        self, field_data: OrderedDict[str, IColumn], mask: Optional[Iterable[bool]]
    ):
        dtype = dt.Struct(
            [dt.Field(n, c.dtype) for n, c in field_data.items()],
            nullable=self.dtype.nullable,
        )
        col = velox.Column(get_velox_type(dtype))
        for n, c in field_data.items():
            col.set_child(col.type().get_child_idx(n), c._data)
            col.set_length(len(c._data))
        if mask is not None:
            mask_list = list(mask)
            assert len(field_data) == 0 or len(mask_list) == len(col)
            for i in range(len(col)):
                if mask_list[i]:
                    col.set_null_at(i)

        return ColumnFromVelox._from_velox(self.device, dtype, col, True)

    def __len__(self):
        return len(self._data)

    @property
    def null_count(self):
        return self._data.get_null_count()

    def _getmask(self, i):
        if i < 0:
            i += len(self._data)
        return self._data.is_null_at(i)

    def _getdata(self, i):
        if i < 0:
            i += len(self._data)
        if not self._getmask(i):
            return tuple(
                ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[j].dtype,
                    self._data.child_at(j),
                    True,
                )._get(i, None)
                for j in range(self._data.children_size())
            )
        else:
            return None

    @staticmethod
    def _valid_mask(ct):
        return np.full((ct,), False, dtype=np.bool8)

    def copy(self):
        return ColumnFromVelox._from_velox(self.device, self.dtype, self._data, True)

    def append(self, values: Iterable[Union[None, dict, tuple]]):
        """Returns column/dataframe with values appended."""
        it = iter(values)

        try:
            value = next(it)
            if value is None:
                if not self.dtype.nullable:
                    raise TypeError(
                        f"a tuple of type {self.dtype} is required, got None"
                    )
                else:
                    df = self.append([{f.name: None for f in self.dtype.fields}])
                    df._data.set_null_at(len(df) - 1)
                    return df

            elif isinstance(value, dict):
                assert self._data.children_size() == len(value)
                res = {}
                for k, v in value.items():
                    idx = self._data.type().get_child_idx(k)
                    child = self._data.child_at(idx)
                    dtype = self.dtype.fields[idx].dtype
                    child_col = ColumnFromVelox._from_velox(
                        self.device, dtype, child, True
                    )
                    child_col = child_col.append([v])
                    res[k] = child_col
                new_data = self._fromdata(res, self._mask + [False])

                return new_data.append(it)

            elif isinstance(value, tuple):
                assert self._data.children_size() == len(value)
                return self.append(
                    [{f.name: v for f, v in zip(self.dtype.fields, value)}]
                ).append(it)
        except StopIteration:
            return self

    def _check_columns(self, columns: Iterable[str]):
        valid_names = {f.name for f in self.dtype.fields}
        for n in columns:
            if n not in valid_names:
                raise TypeError(f"column {n} not among existing dataframe columns")

    # implementing abstract methods ----------------------------------------------

    def _set_field_data(self, name: str, col: IColumn, empty_df: bool):
        if not empty_df and len(col) != len(self):
            raise TypeError("all columns/lists must have equal length")

        column_idx = self._dtype.get_index(name)
        new_delegate = velox.Column(get_velox_type(self._dtype))
        new_delegate.set_length(len(col._data))

        # Set columns for new_delegate
        for idx in range(len(self._dtype.fields)):
            if idx != column_idx:
                new_delegate.set_child(idx, self._data.child_at(idx))
            else:
                new_delegate.set_child(idx, col._data)

        self._data = new_delegate

    # printing ----------------------------------------------------------------

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        data = []
        for i in self:
            if i is None:
                data.append(["None"] * len(self.columns))
            else:
                assert len(i) == len(self.columns)
                data.append(list(i))
        tab = tabulate(
            data, headers=["index"] + self.columns, tablefmt="simple", showindex=True
        )
        typ = f"dtype: {self._dtype}, count: {len(self)}, null_count: {self.null_count}"
        return tab + dt.NL + typ

    # selectors -----------------------------------------------------------

    def _column_index(self, arg):
        return self._data.type().get_child_idx(arg)

    def _gets(self, indices):
        return self._fromdata(
            {n: c[indices] for n, c in self._field_data.items()}, self._mask[indices]
        )

    def _slice(self, start, stop, step):
        mask = [self._mask[i] for i in list(range(len(self)))[start:stop:step]]
        return self._fromdata(
            {
                self.dtype.fields[i]
                .name: ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
                ._slice(start, stop, step)
                for i in range(self._data.children_size())
            },
            mask,
        )

    def get_column(self, column):
        idx = self._data.type().get_child_idx(column)
        return ColumnFromVelox._from_velox(
            self.device,
            self.dtype.fields[idx].dtype,
            self._data.child_at(idx),
            True,
        )

    def get_columns(self, columns):
        # TODO: decide on nulls, here we assume all defined (mask = False) for new parent...
        res = {}
        for n in columns:
            res[n] = self.get_column(n)
        return self._fromdata(res, self._mask)

    def slice_columns(self, start, stop):
        # TODO: decide on nulls, here we assume all defined (mask = False) for new parent...
        _start = 0 if start is None else self._column_index(start)
        _stop = len(self.columns) if stop is None else self._column_index(stop)
        res = {}
        for i in range(_start, _stop):
            m = self.columns[i]
            res[m] = ColumnFromVelox._from_velox(
                self.device,
                self.dtype.fields[i].dtype,
                self._data.child_at(i),
                True,
            )
        return self._fromdata(res, self._mask)

    # functools map/filter/reduce ---------------------------------------------

    @trace
    @expression
    def map(
        self,
        arg: Union[Dict, Callable],
        na_action=None,
        dtype: Optional[dt.DType] = None,
        columns: Optional[List[str]] = None,
    ):
        """
        Maps rows according to input correspondence.
        dtype required if result type != item type.
        """

        if columns is None:
            return super().map(arg, na_action, dtype)
        self._check_columns(columns)

        if len(columns) == 1:
            idx = self._data.type().get_child_idx(columns[0])
            return ColumnFromVelox._from_velox(
                self.device,
                self.dtype.fields[idx].dtype,
                self._data.child_at(idx),
                True,
            ).map(arg, na_action, dtype)

        if not isinstance(arg, dict) and dtype is None:
            (dtype, _) = dt.infer_dype_from_callable_hint(arg)
        dtype = dtype or self._dtype

        cols = []
        for n in columns:
            idx = self._data.type().get_child_idx(n)
            cols.append(
                ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[idx].dtype,
                    self._data.child_at(idx),
                    True,
                )
            )

        # Faster path (for the very slow python path)
        if all([col.null_count == 0 for col in cols]) and not (isinstance(arg, dict)):
            res = []
            dcols = [col._data for col in cols]
            if len(dcols) == 2:
                a, b = dcols[0], dcols[1]
                res = [arg(a[i], b[i]) for i in range(len(a))]
            elif len(dcols) == 3:
                a, b, c = dcols[0], dcols[1], dcols[2]
                res = [arg(a[i], b[i], c[i]) for i in range(len(a))]
            else:
                res = [arg(*[dcol[i] for dcol in dcols]) for i in range(len(dcols[0]))]
            return Scope._FromPyList(res, dtype)

        # Slow path for very slow path
        def func(*x):
            return arg.get(tuple(*x), None) if isinstance(arg, dict) else arg(*x)

        res = []
        for i in range(len(self)):
            if all([col.is_valid_at(i) for col in cols]) or (na_action is None):
                res.append(func(*[col[i] for col in cols]))
            elif na_action == "ignore":
                res.append(None)
            else:
                raise TypeError(f"na_action has unsupported value {na_action}")
        return Scope._FromPyList(res, dtype)

    @trace
    @expression
    def flatmap(
        self,
        arg: Union[Dict, Callable],
        na_action=None,
        dtype: Optional[dt.DType] = None,
        columns: Optional[List[str]] = None,
    ):
        """
        Maps rows to list of rows according to input correspondence
        dtype required if result type != item type.
        """
        if columns is None:
            return super().flatmap(arg, na_action, dtype)
        self._check_columns(columns)

        if len(columns) == 1:
            return self._field_data[columns[0]].flatmap(
                arg,
                na_action,
                dtype,
            )
        else:

            def func(x):
                return arg.get(x, None) if isinstance(arg, dict) else arg(x)

            dtype_ = dtype if dtype is not None else self._dtype
            cols = [self._field_data[n] for n in columns]
            res = Scope._EmptyColumn(dtype_)
            for i in range(len(self)):
                if self.valid(i):
                    res._extend(func(*[col[i] for col in cols]))
                elif na_action is None:
                    res._extend(func(None))
                else:
                    res._append([])
            return res._finalize()

    @trace
    @expression
    def filter(
        self, predicate: Union[Callable, Iterable], columns: Optional[List[str]] = None
    ):
        """
        Select rows where predicate is True.
        Different from Pandas. Use keep for Pandas filter.

        Parameters
        ----------
        predicate - callable or iterable
            A predicate function or iterable of booleans the same
            length as the column.  If an n-ary predicate, use the
            columns parameter to provide arguments.
        columns - list of string names, default None
            Which columns to invoke the filter with.  If None, apply to
            all columns.

        See Also
        --------
        map, reduce, flatmap

        Examples
        --------
        >>> ta.Column([1,2,3,4]).filter([True, False, True, False]) == ta.Column([1,2,3,4]).filter(lambda x: x%2==1)
        0  1
        1  1
        dtype: boolean, length: 2, null_count: 0
        """
        if columns is None:
            return super().filter(predicate)

        self._check_columns(columns)

        if not isinstance(predicate, Iterable) and not callable(predicate):
            raise TypeError(
                "predicate must be a unary boolean predicate or iterable of booleans"
            )

        res = Scope._EmptyColumn(self._dtype)
        cols = []
        for n in columns:
            idx = self._data.type().get_child_idx(n)
            cols.append(
                ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[idx].dtype,
                    self._data.child_at(idx),
                    True,
                )
            )
        if callable(predicate):
            for i in range(len(self)):
                if predicate(*[col[i] for col in cols]):
                    res._append(self[i])
        elif isinstance(predicate, Iterable):
            for x, p in zip(self, predicate):
                if p:
                    res._append(x)
        else:
            pass
        return res._finalize()

    # sorting ----------------------------------------------------------------

    @trace
    @expression
    def sort(
        self,
        by: Optional[List[str]] = None,
        ascending=True,
        na_position="last",
    ):
        """Sort a column/a dataframe in ascending or descending order"""
        # Not allowing None in comparison might be too harsh...
        # Move all rows with None that in sort index to back...
        func = None
        if isinstance(by, list):
            xs = []
            for i in by:
                _ = self._data.type().get_child_idx(i)  # throws key error
                xs.append(self.columns.index(i))
            reorder = xs + [j for j in range(len(self.dtype.fields)) if j not in xs]

            def func(tup):
                return tuple(tup[i] for i in reorder)

        res = Scope._EmptyColumn(self.dtype)
        if na_position == "first":
            res._extend([None] * self.null_count)
        res._extend(
            sorted((i for i in self if i is not None), reverse=not ascending, key=func)
        )
        if na_position == "last":
            res._extend([None] * self.null_count)
        return res._finalize()

    @trace
    @expression
    def _nlargest(
        self,
        n=5,
        columns: Optional[List[str]] = None,
        keep="first",
    ):
        """Returns a new dataframe of the *n* largest elements."""
        # Todo add keep arg
        return self.sort(by=columns, ascending=False).head(n)

    @trace
    @expression
    def _nsmallest(
        self,
        n=5,
        columns: Optional[List[str]] = None,
        keep="first",
    ):
        """Returns a new dataframe of the *n* smallest elements."""
        return self.sort(by=columns, ascending=True).head(n)

    # operators --------------------------------------------------------------

    @expression
    def __add__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    + ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    + other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __radd__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: other[n] + c for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: other
                    + ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __sub__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    - ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    - other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __rsub__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    - ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: other
                    - ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __mul__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    * ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    * other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __rmul__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    * ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: other
                    * ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __floordiv__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    // ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    // other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __rfloordiv__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    // ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: other
                    // ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __truediv__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    / ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    / other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __rtruediv__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: other[n] / c for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata({n: other / c for (n, c) in self._field_data.items()})

    @expression
    def __mod__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: c % other[n] for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    % other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __rmod__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: other[n] % c for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata({n: other % c for (n, c) in self._field_data.items()})

    @expression
    def __pow__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    ** ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    ** other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __rpow__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    ** ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: other
                    ** ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __eq__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    == ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    == other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __ne__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: c == other[n] for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata(
                {n: c == other for (n, c) in self._field_data.items()}
            )

    @expression
    def __lt__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    < ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    < other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    @expression
    def __gt__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    > ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    > other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    def __le__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: c <= other[n] for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    <= other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    def __ge__(self, other):
        if isinstance(other, DataFrameCpu):
            assert len(self) == len(other)
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    >= ColumnFromVelox._from_velox(
                        other.device,
                        other.dtype.fields[i].dtype,
                        other._data.child_at(i),
                        True,
                    )
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            return self._fromdata(
                {n: c >= other for (n, c) in self._field_data.items()}
            )

    def __or__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: c | other[n] for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata(
                {
                    self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    | other
                    for i in range(self._data.children_size())
                },
                self._mask,
            )

    def __ror__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: other[n] | c for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata({n: other | c for (n, c) in self._field_data.items()})

    def __and__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: c & other[n] for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata({n: c & other for (n, c) in self._field_data.items()})

    def __rand__(self, other):
        if isinstance(other, DataFrameCpu):
            return self._fromdata(
                {n: other[n] & c for (n, c) in self._field_data.items()}
            )
        else:
            return self._fromdata({n: other & c for (n, c) in self._field_data.items()})

    def __invert__(self):
        return self._fromdata({n: ~c for (n, c) in self._field_data.items()})

    def __neg__(self):
        return self._fromdata(
            {
                self.dtype.fields[i].name: -ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
                for i in range(self._data.children_size())
            },
            self._mask,
        )

    def __pos__(self):
        return self._fromdata(
            {
                self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
                for i in range(self._data.children_size())
            },
            self._mask,
        )

    # isin ---------------------------------------------------------------

    @trace
    @expression
    def isin(self, values: Union[list, dict, IColumn]):
        """Check whether values are contained in data."""
        if isinstance(values, list):
            return self._fromdata(
                {
                    self.dtype.fields[i]
                    .name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    .isin(values)
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        if isinstance(values, dict):
            self._check_columns(values.keys())
            return self._fromdata(
                {n: c.isin(values[n]) for n, c in self._field_data.items()}
            )
        if isinstance(values, IDataFrame):
            self._check_columns(values.columns)
            return self._fromdata(
                {n: c.isin(values=list(values[n])) for n, c in self._field_data.items()}
            )
        else:
            raise ValueError(
                f"isin undefined for values of type {type(self).__name__}."
            )

    # data cleaning -----------------------------------------------------------

    @trace
    @expression
    def fill_null(self, fill_value: Optional[Union[dt.ScalarTypes, Dict]]):
        if fill_value is None:
            return self
        if isinstance(fill_value, IColumn._scalar_types):
            return self._fromdata(
                {
                    self.dtype.fields[i]
                    .name: ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                    .fill_null(fill_value)
                    for i in range(self._data.children_size())
                },
                self._mask,
            )
        else:
            raise TypeError(f"fill_null with {type(fill_value)} is not supported")

    @trace
    @expression
    def drop_null(self, how="any"):
        """Return a dataframe with rows removed where the row has any or all nulls."""
        self._prototype_support_warning("drop_null")

        # TODO only flat columns supported...
        assert self._dtype is not None
        res = Scope._EmptyColumn(self._dtype.constructor(nullable=False))
        if how == "any":
            for i in self:
                if not self._has_any_null(i):
                    res._append(i)
        elif how == "all":
            for i in self:
                if not self._has_all_null(i):
                    res._append(i)
        return res._finalize()

    @trace
    @expression
    def drop_duplicates(
        self,
        subset: Optional[List[str]] = None,
        keep="first",
    ):
        """Remove duplicate values from data but keep the first, last, none (keep=False)"""
        self._prototype_support_warning("drop_duplicates")

        columns = subset if subset is not None else self.columns
        self._check_columns(columns)

        # TODO fix slow implementation by vectorization,
        # i.e do unique per column and delete when all agree
        # shortcut once no match is found.

        res = Scope._EmptyColumn(self.dtype)
        indices = [self.columns.index(s) for s in columns]
        seen = set()
        for tup in self:
            row = tuple(tup[i] for i in indices)
            if row in seen:
                continue
            else:
                seen.add(row)
                res._append(tup)
        return res._finalize()

    # @staticmethod
    def _has_any_null(self, tup) -> bool:
        for t in tup:
            if t is None:
                return True
            if isinstance(t, tuple) and self._has_any_null(t):
                return True
        return False

    # @staticmethod
    def _has_all_null(self, tup) -> bool:
        for t in tup:
            if t is not None:
                return False
            if isinstance(t, tuple) and not self._has_all_null(t):
                return False
        return True

    # universal ---------------------------------------------------------

    # TODO Decide on tracing level: If we trace  'min' om a
    # - highlevel then we can use lambdas inside min
    # - lowelevel, i.e call 'summarize', then lambdas have to become
    #   - global functions if they have no state
    #   - dataclasses with an apply function if they have state

    @staticmethod
    def _cmin(c):
        return c.min

    # with static function

    @trace
    @expression
    def min(self):
        """Return the minimum of the non-null values of the Column."""
        return self._summarize(DataFrameCpu._cmin)

    # with dataclass function
    # @expression
    # def min(self, numeric_only=None):
    #     """Return the minimum of the non-null values of the Column."""
    #     return self._summarize(_Min(), {"numeric_only": numeric_only})

    # with lambda
    # @expression
    # def min(self, numeric_only=None):
    #     """Return the minimum of the non-null values of the Column."""
    #     return self._summarize(lambda c: c.min, {"numeric_only": numeric_only})

    @trace
    @expression
    def max(self):
        """Return the maximum of the non-null values of the column."""
        # skipna == True
        return self._summarize(lambda c: c.max)

    @trace
    @expression
    def all(self):
        """Return whether all non-null elements are True in Column"""
        return self._summarize(lambda c: c.all)

    @trace
    @expression
    def any(self):
        """Return whether any non-null element is True in Column"""
        return self._summarize(lambda c: c.any)

    @trace
    @expression
    def sum(self):
        """Return sum of all non-null elements in Column"""
        return self._summarize(lambda c: c.sum)

    @trace
    @expression
    def _cummin(self):
        """Return cumulative minimum of the data."""
        return self._lift(lambda c: c._cummin)

    @trace
    @expression
    def _cummax(self):
        """Return cumulative maximum of the data."""
        return self._lift(lambda c: c._cummax)

    @trace
    @expression
    def cumsum(self):
        """Return cumulative sum of the data."""
        return self._lift(lambda c: c.cumsum)

    @trace
    @expression
    def _cumprod(self):
        """Return cumulative product of the data."""
        return self._lift(lambda c: c._cumprod)

    @trace
    @expression
    def mean(self):
        """Return the mean of the values in the series."""
        return self._summarize(lambda c: c.mean)

    @trace
    @expression
    def median(self):
        """Return the median of the values in the data."""
        return self._summarize(lambda c: c.median)

    @trace
    @expression
    def mode(self):
        """Return the mode(s) of the data."""
        return self._summarize(lambda c: c.mode)

    @trace
    @expression
    def std(self):
        """Return the stddev(s) of the data."""
        return self._summarize(lambda c: c.std)

    @trace
    @expression
    def _nunique(self, drop_null=True):
        """Returns the number of unique values per column"""
        res = {}
        res["column"] = ta.Column([f.name for f in self.dtype.fields], dt.string)
        res["unique"] = ta.Column(
            [
                ColumnFromVelox._from_velox(
                    self.device,
                    f.dtype,
                    self._data.child_at(self._data.type().get_child_idx(f.name)),
                    True,
                )._nunique(drop_null)
                for f in self.dtype.fields
            ],
            dt.int64,
        )
        return self._fromdata(res, None)

    def _summarize(self, func):
        res = ta.Column(self.dtype)

        for i in range(self._data.children_size()):
            result = func(
                ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
            )()
            if result is None:
                res._data.child_at(i).append_null()
            else:
                res._data.child_at(i).append(result)
        res._data.set_length(1)
        return res

    @trace
    def _lift(self, func):
        if self.null_count == 0:
            res = velox.Column(get_velox_type(self.dtype))

            for i in range(self._data.children_size()):
                child = func(
                    ColumnFromVelox._from_velox(
                        self.device,
                        self.dtype.fields[i].dtype,
                        self._data.child_at(i),
                        True,
                    )
                )()
                res.set_child(
                    i,
                    child._data,
                )
            res.set_length(len(self._data))
            return ColumnFromVelox._from_velox(self.device, self.dtype, res, True)
        raise NotImplementedError("Dataframe row is not allowed to have nulls")

    # describe ----------------------------------------------------------------

    @trace
    @expression
    def describe(
        self,
        percentiles=None,
        include=None,
        exclude=None,
    ):
        """Generate descriptive statistics."""
        # Not supported: datetime_is_numeric=False,
        includes = []
        if include is None:
            includes = [f.name for f in self.dtype.fields if dt.is_numerical(f.dtype)]
        elif isinstance(include, list):
            includes = [f.name for f in self.dtype.fields if f.dtype in include]
        else:
            raise TypeError(
                f"describe with include of type {type(include).__name__} is not supported"
            )

        excludes = []
        if exclude is None:
            excludes = []
        elif isinstance(exclude, list):
            excludes = [f.name for f in self.dtype.fields if f.dtype in exclude]
        else:
            raise TypeError(
                f"describe with exclude of type {type(exclude).__name__} is not supported"
            )
        selected = [i for i in includes if i not in excludes]

        if percentiles is None:
            percentiles = [25, 50, 75]
        percentiles = sorted(set(percentiles))
        if len(percentiles) > 0:
            if percentiles[0] < 0 or percentiles[-1] > 100:
                raise ValueError("percentiles must be betwen 0 and 100")

        res = {}
        res["metric"] = ta.Column(
            ["count", "mean", "std", "min"] + [f"{p}%" for p in percentiles] + ["max"]
        )
        for s in selected:
            idx = self._data.type().get_child_idx(s)
            c = ColumnFromVelox._from_velox(
                self.device,
                self.dtype.fields[idx].dtype,
                self._data.child_at(idx),
                True,
            )
            res[s] = ta.Column(
                [c._count(), c.mean(), c.std(), c.min()]
                + c._quantile(percentiles, "midpoint")
                + [c.max()]
            )
        return self._fromdata(res, [False] * len(res["metric"]))

    # Dataframe specific ops --------------------------------------------------    #

    @trace
    @expression
    def drop(self, columns: List[str]):
        self._check_columns(columns)
        return self._fromdata(
            {
                self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
                for i in range(self._data.children_size())
                if self.dtype.fields[i].name not in columns
            },
            self._mask,
        )

    @trace
    @expression
    def keep(self, columns: List[str]):
        """
        Returns DataFrame with the kept columns only.
        """
        self._check_columns(columns)
        return self._fromdata(
            {
                self.dtype.fields[i].name: ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
                for i in range(self._data.children_size())
                if self.dtype.fields[i].name in columns
            },
            self._mask,
        )

    @trace
    @expression
    def rename(self, column_mapper: Dict[str, str]):
        self._check_columns(column_mapper.keys())
        return self._fromdata(
            {
                column_mapper.get(
                    self.dtype.fields[i].name, self.dtype.fields[i].name
                ): ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
                for i in range(self._data.children_size())
            },
            self._mask,
        )

    @trace
    @expression
    def reorder(self, columns: List[str]):
        """
        Returns DataFrame with the columns in the prescribed order.
        """
        self._check_columns(columns)
        return self._fromdata(
            {
                col: ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[self._data.type().get_child_idx(col)].dtype,
                    self._data.child_at(self._data.type().get_child_idx(col)),
                    True,
                )
                for col in columns
            },
            self._mask,
        )

    # interop ----------------------------------------------------------------

    def to_pandas(self):
        """Convert self to pandas dataframe"""
        # TODO Add type translation.
        # Skipping analyzing 'pandas': found module but no type hints or library stubs
        import pandas as pd  # type: ignore

        data = {}
        for n, c in self._field_data.items():
            data[n] = c.to_pandas()
        return pd.DataFrame(data)

    def to_arrow(self):
        """Convert self to arrow table"""
        # TODO Add type translation
        import pyarrow as pa  # type: ignore

        data = {}
        fields = []
        for i in range(0, self._data.children_size()):
            name = self.dtype.fields[i].name
            column = ColumnFromVelox._from_velox(
                self.device,
                self.dtype.fields[i].dtype,
                self._data.child_at(i),
                True,
            )
            arrow_array = column.to_arrow()
            data[name] = arrow_array
            fields.append(
                pa.field(name, arrow_array.type, nullable=column.dtype.nullable)
            )

        return pa.table(data, schema=pa.schema(fields))

    def to_torch(self, conversion=None):
        pytorch.ensure_available()

        conversion = conversion or {}
        if isinstance(conversion, pytorch.ITorchConversion):
            return conversion.to_torch(self)

        assert isinstance(conversion, dict)
        # TODO: this actually puts the type annotations on the tuple wrong.
        # We might need to address it eventually, but because it's Python it doesn't matter
        tup_type = self._dtype.py_type

        return tup_type(
            *(
                conversion.get(f.name, pytorch.DefaultTorchConversion()).to_torch(
                    self[f.name]
                )
                for f in self.dtype.fields
            )
        )

    def _to_torch_default(self):
        return self.to_torch()

    # fluent with symbolic expressions ----------------------------------------

    # TODO decide on whether we nat to have arbitrarily nested wheres...
    @trace
    @expression
    def where(self, *conditions):
        """
        Analogous to SQL's where (NOT Pandas where)

        Filter a dataframe to only include rows satisfying a given set
        of conditions. df.where(p) is equivalent to writing df[p].

        Examples
        --------

        >>> from torcharrow import ta
        >>> xf = ta.DataFrame({
        >>>    'A':['a', 'b', 'a', 'b'],
        >>>    'B': [1, 2, 3, 4],
        >>>    'C': [10,11,12,13]})
        >>> xf.where(xf['B']>2)
          index  A      B    C
        -------  ---  ---  ---
              0  a      3   12
              1  b      4   13
        dtype: Struct([Field('A', string), Field('B', int64), Field('C', int64)]), count: 2, null_count: 0

        When referring to self in an expression, the special value `me` can be
        used.

        >>> from torcharrow import me
        >>> xf.where(me['B']>2)
          index  A      B    C
        -------  ---  ---  ---
              0  a      3   12
              1  b      4   13
        dtype: Struct([Field('A', string), Field('B', int64), Field('C', int64)]), count: 2, null_count: 0
        """

        if len(conditions) == 0:
            return self

        values = []
        for i, condition in enumerate(conditions):
            value = eval_expression(condition, {"me": self})
            values.append(value)

        reduced_values = functools.reduce(lambda x, y: x & y, values)
        return self[reduced_values]

    @trace
    @expression
    def select(self, *args, **kwargs):
        """
        Analogous to SQL's ``SELECT`.

        Transform a dataframe by selecting old columns and new (computed)
        columns.

        args - positional string arguments
            Column names to keep in the projection. A column name of "*" is a
            shortcut to denote all columns. A column name beginning with "-"
            means remove this column.

        kwargs - named value arguments
            New column name expressions to add to the projection

        The special symbol me can  be used to refer to self.

        Examples
        --------
        >>> from torcharrow import ta
        >>> xf = ta.DataFrame({
        >>>    'A': ['a', 'b', 'a', 'b'],
        >>>    'B': [1, 2, 3, 4],
        >>>    'C': [10,11,12,13]})
        >>> xf.select(*xf.columns,D=me['B']+me['C'])
          index  A      B    C    D
        -------  ---  ---  ---  ---
              0  a      1   10   11
              1  b      2   11   13
              2  a      3   12   15
              3  b      4   13   17
        dtype: Struct([Field('A', string), Field('B', int64), Field('C', int64), Field('D', int64)]), count: 4, null_count: 0

        Using '*' and '-colname':

        >>> xf.select('*','-B',D=me['B']+me['C'])
          index  A      C    D
        -------  ---  ---  ---
              0  a     10   11
              1  b     11   13
              2  a     12   15
              3  b     13   17
        dtype: Struct([Field('A', string), Field('C', int64), Field('D', int64)]), count: 4, null_count: 0
        """

        input_columns = set(self.columns)

        has_star = False
        include = []
        exclude = []
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("args must be column names")
            if arg == "*":
                if has_star:
                    raise ValueError("select received repeated stars")
                has_star = True
            elif arg in input_columns:
                if arg in include:
                    raise ValueError(
                        f"select received a repeated column-include ({arg})"
                    )
                include.append(arg)
            elif arg[0] == "-" and arg[1:] in input_columns:
                if arg in exclude:
                    raise ValueError(
                        f"select received a repeated column-exclude ({arg[1:]})"
                    )
                exclude.append(arg[1:])
            else:
                raise ValueError(f"argument ({arg}) does not denote an existing column")
        if exclude and not has_star:
            raise ValueError("select received column-exclude without a star")
        if has_star and include:
            raise ValueError("select received both a star and column-includes")
        if set(include) & set(exclude):
            raise ValueError(
                "select received overlapping column-includes and " + "column-excludes"
            )

        include_inc_star = self.columns if has_star else include

        output_columns = [col for col in include_inc_star if col not in exclude]

        res = {}
        for i in range(self._data.children_size()):
            n = self.dtype.fields[i].name
            if n in output_columns:
                res[n] = ColumnFromVelox._from_velox(
                    self.device,
                    self.dtype.fields[i].dtype,
                    self._data.child_at(i),
                    True,
                )
        for n, c in kwargs.items():
            res[n] = eval_expression(c, {"me": self})
        return self._fromdata(res, self._mask)

    @trace
    @expression
    def pipe(self, func, *args, **kwargs):
        """
        Apply func(self, *args, **kwargs).
        """
        return func(self, *args, **kwargs)

    @trace
    @expression
    def groupby(
        self,
        by: List[str],
        sort=False,
        drop_null=True,
    ):
        """
        SQL like data grouping, supporting split-apply-combine paradigm.

        Parameters
        ----------
        by - list of strings
            List of column names to group by.

        sort - bool
            Whether the groups are in sorted order.

        drop_null - bool
            Whether NULL/NaNs in group keys are dropped.

        Examples
        --------
        >>> import torcharrow as ta
        >>> df = ta.DataFrame({'A': ['a', 'b', 'a', 'b'], 'B': [1, 2, 3, 4]})
        >>> # group by A
        >>> grouped = df.groupby(['A'])
        >>> # apply sum on each of B's grouped column to create a new column
        >>> grouped_sum = grouped['B'].sum()
        >>> # combine a new dataframe from old and new columns
        >>> res = ta.DataFrame()
        >>> res['A'] = grouped['A']
        >>> res['B.sum'] = grouped_sum
        >>> res
          index  A      B.sum
        -------  ---  -------
              0  a          4
              1  b          6
        dtype: Struct([Field('A', string), Field('B.sum', int64)]), count: 2, null_count: 0

        The same as above, as a one-liner:

        >>> df.groupby(['A']).sum()
          index  A      B.sum
        -------  ---  -------
              0  a          4
              1  b          6
        dtype: Struct([Field('A', string), Field('B.sum', int64)]), count: 2, null_count: 0

        To apply multiple aggregate functions to different parts of the
        dataframe, use groupby followed by select.


        >>> df = ta.DataFrame({
        >>>    'A':['a', 'b', 'a', 'b'],
        >>>    'B': [1, 2, 3, 4],
        >>>    'C': [10,11,12,13]})
        >>> df.groupby(['A']).select(b_sum=me['B'].sum(), c_count=me['C'].count())
          index  A      b_sum    c_count
        -------  ---  -------  ---------
              0  a          4          2
              1  b          6          2
        dtype: Struct([Field('A', string), Field('b_sum', int64), Field('c_count', int64)]), count: 2, null_count: 0

        To see what data groups contain:

        >>> for g, df in grouped:
                print(g)
                print("   ", df)
        ('a',)
           self._fromdata({'B':Column([1, 3], id = c129), id = c130})
        ('b',)
           self._fromdata({'B':Column([2, 4], id = c131), id = c132})
        """
        self._prototype_support_warning("groupby")

        # TODO implement
        assert not sort
        assert drop_null
        self._check_columns(by)

        key_columns = by
        key_fields = []
        item_fields = []
        for k in key_columns:
            key_fields.append(dt.Field(k, self.dtype.get(k)))
        for f in self.dtype.fields:
            if f.name not in key_columns:
                item_fields.append(f)

        groups: Dict[Tuple, ar.array] = {}
        for i in range(len(self)):
            if self.is_valid_at(i):
                key = tuple(
                    self._data.child_at(self._data.type().get_child_idx(f.name))[i]
                    for f in key_fields
                )
                if key not in groups:
                    groups[key] = ar.array("I")
                df = groups[key]
                df.append(i)
            else:
                pass
        return GroupedDataFrame(key_fields, item_fields, groups, self)


@dataclass
class GroupedDataFrame:
    _key_fields: List[dt.Field]
    _item_fields: List[dt.Field]
    _groups: Mapping[Tuple, Sequence]
    _parent: DataFrameCpu

    @property
    def _scope(self):
        return self._parent._scope

    @property  # type: ignore
    @traceproperty
    def size(self):
        """
        Return the size of each group (including nulls).
        """
        res = {
            f.name: ta.Column([v[idx] for v, _ in self._groups.items()], f.dtype)
            for idx, f in enumerate(self._key_fields)
        }

        res["size"] = ta.Column([len(c) for _, c in self._groups.items()], dt.int64)

        return self._parent._fromdata(res, None)

    def __iter__(self):
        """
        Yield pairs of grouped tuple and the grouped dataframe
        """
        for g, xs in self._groups.items():
            dtype = dt.Struct(self._item_fields)
            df = ta.Column(dtype).append(
                tuple(
                    tuple(
                        self._parent._data.child_at(
                            self._parent._data.type().get_child_idx(f.name)
                        )[x]
                        for f in self._item_fields
                    )
                    for x in xs
                )
            )

            yield g, df

    @trace
    def _lift(self, op: str) -> IColumn:
        if len(self._key_fields) > 0:
            # it is a dataframe operation:
            return self._combine(op)
        elif len(self._item_fields) == 1:
            return self._apply1(self._item_fields[0], op)
        raise AssertionError("unexpected case")

    def _combine(self, op: str):
        agg_fields = [dt.Field(f"{f.name}.{op}", f.dtype) for f in self._item_fields]
        res = {}
        for f, c in zip(self._key_fields, self._unzip_group_keys()):
            res[f.name] = c
        for f, c in zip(agg_fields, self._apply(op)):
            res[f.name] = c
        return self._parent._fromdata(res, None)

    def _apply(self, op: str) -> List[IColumn]:
        cols = []
        for f in self._item_fields:
            cols.append(self._apply1(f, op))
        return cols

    def _apply1(self, f: dt.Field, op: str) -> IColumn:
        src_t = f.dtype
        dest_f, dest_t = dt.get_agg_op(op, src_t)
        res = Scope._EmptyColumn(dest_t)
        src_c = self._parent._data.child_at(
            self._parent._data.type().get_child_idx(f.name)
        )
        for g, xs in self._groups.items():
            dest_data = [src_c[x] for x in xs]
            dest_c = dest_f(ta.Column(dest_data, dtype=dest_t))
            res._append(dest_c)
        return res._finalize()

    def _unzip_group_keys(self) -> List[IColumn]:
        cols = []
        for f in self._key_fields:
            cols.append(Scope._EmptyColumn(f.dtype))
        for tup in self._groups.keys():
            for i, t in enumerate(tup):
                cols[i]._append(t)
        return [col._finalize() for col in cols]

    def __contains__(self, key: str):
        for f in self._item_fields:
            if f.name == key:
                return True
        for f in self._key_fields:
            if f.name == key:
                return True
        return False

    def __getitem__(self, arg):
        """
        Return the named grouped column
        """
        # TODO extend that this works inside struct frames as well,
        # e.g. grouped['a']['b'] where grouped returns a struct column having 'b' as field
        if isinstance(arg, str):
            for f in self._item_fields:
                if f.name == arg:
                    return GroupedDataFrame([], [f], self._groups, self._parent)
            for i, f in enumerate(self._key_fields):
                if f.name == arg:
                    res = Scope._EmptyColumn(f.dtype)
                    for tup in self._groups.keys():
                        res._append(tup[i])
                    return res._finalize()
            raise ValueError(f"no column named ({arg}) in grouped dataframe")
        raise TypeError(f"unexpected type for arg ({type(arg).__name})")

    def min(self, numeric_only=None):
        """Return the minimum of the non-null values of the Column."""
        assert numeric_only == None
        return self._lift("min")

    def max(self, numeric_only=None):
        """Return the minimum of the non-null values of the Column."""
        assert numeric_only == None
        return self._lift("min")

    def all(self, boolean_only=None):
        """Return whether all non-null elements are True in Column"""
        # skipna == True
        return self._lift("all")

    def any(self, skipna=True, boolean_only=None):
        """Return whether any non-null element is True in Column"""
        # skipna == True
        return self._lift("any")

    def sum(self):
        """Return sum of all non-null elements in Column"""
        # skipna == True
        # only_numerical == True
        # skipna == True
        return self._lift("sum")

    def mean(self):
        """Return the mean of the values in the series."""
        return self._lift("mean")

    def median(self):
        """Return the median of the values in the data."""
        return self._lift("median")

    def mode(self):
        """Return the mode(s) of the data."""
        return self._lift("mode")

    def std(self):
        """Return the stddev(s) of the data."""
        return self._lift("std")

    def count(self):
        """Return the count(s) of the data."""
        return self._lift("count")

    # TODO should add reduce here as well...

    @trace
    def agg(self, arg):
        """
        Apply aggregation(s) to the groups.
        """
        # DataFrame{'a': [1, 1, 2], 'b': [1, 2, 3], 'c': [2, 2, 1]})
        # a.groupby('a').agg('sum') -- applied on rest
        # a.groupby('a').agg(['sum', 'min']) -- both applied on rest
        # a.groupby('a').agg({'b': ['min', 'mean']}) -- applied on
        # TODO
        # a.groupby('a').aggregate( a= me['a'].mean(), b_min =me['b'].min(), b_mean=me['c'].mean()))
        # f1 = lambda x: x._quantile(0.5); f1.__name__ = "q0.5"
        # f2 = lambda x: x._quantile(0.75); f2.__name__ = "q0.75"
        # a.groupby('a').agg([f1, f2])

        res = {}
        for f, c in zip(self._key_fields, self._unzip_group_keys()):
            res[f.name] = c
        for agg_name, field, op in self._normalize_agg_arg(arg):
            res[agg_name] = self._apply1(field, op)
        return self._parent._fromdata(res, None)

    def aggregate(self, arg):
        """
        Apply aggregation(s) to the groups.
        """
        return self.agg(arg)

    @trace
    def select(self, **kwargs):
        """
        Like select for dataframes, except for groups
        """

        res = {}
        for f, c in zip(self._key_fields, self._unzip_group_keys()):
            res[f.name] = c
        for n, c in kwargs.items():
            res[n] = eval_expression(c, {"me": self})
        return self._parent._fromdata(res)

    def _normalize_agg_arg(self, arg):
        res = []  # triple name, field, op
        if isinstance(arg, str):
            # normalize
            arg = [arg]
        if isinstance(arg, list):
            for op in arg:
                for f in self._item_fields:
                    res.append((f"{f.name}.{op}", f, op))
        elif isinstance(arg, dict):
            for n, ops in arg.items():
                fields = [f for f in self._item_fields if f.name == n]
                if len(fields) == 0:
                    raise ValueError(f"column ({n}) does not exist")
                # TODO handle duplicate columns, if ever...
                assert len(fields) == 1
                if isinstance(ops, str):
                    ops = [ops]
                for op in ops:
                    res.append((f"{n}.{op}", fields[0], op))
        else:
            raise TypeError(f"unexpected arg type ({type(arg).__name__})")
        return res


# ------------------------------------------------------------------------------
# registering the factory

Dispatcher.register((dt.Struct.typecode + "_empty", "cpu"), DataFrameCpu._empty)
Dispatcher.register((dt.Struct.typecode + "_full", "cpu"), DataFrameCpu._full)
Dispatcher.register((dt.Struct.typecode + "_fromlist", "cpu"), DataFrameCpu._fromlist)


# ------------------------------------------------------------------------------
# DataFrame var (is here and not in Expression) to break cyclic import dependency


# ------------------------------------------------------------------------------
# Relational operators, still TBD


#         def join(
#             self,
#             other,
#             on=None,
#             how="left",
#             lsuffix="",
#             rsuffix="",
#             sort=False,
#             method="hash",
#         ):
#         """Join columns with other DataFrame on index or on a key column."""


#     def rolling(
#         self, window, min_periods=None, center=False, axis=0, win_type=None
#     ):
#         return Rolling(
#             self,
#             window,
#             min_periods=min_periods,
#             center=center,
#             axis=axis,
#             win_type=win_type,
#         )

#
#       all set operations: union, uniondistinct, except, etc.
