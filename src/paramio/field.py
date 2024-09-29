from __future__ import annotations

import dataclasses

from . import entries, prototype, types, view
from ._internal import typing
from .types import var


class Params(typing.TypedDict, total=False):
    key: tuple[str, ...]
    default: typing.Any
    reader: types.ReaderType[typing.Any, typing.Any]
    converter: types.ConverterType[typing.Any, typing.Any]


@dataclasses.dataclass(slots=True)
class FieldBuilder(
    types.FieldBuilderType[prototype.Prototype, typing.Never, var.OutType],
    typing.Generic[var.KeyType, var.OutType],
):
    key: var.KeyType
    default: var.OutType
    reader: types.ReaderType[var.KeyType, typing.Any]
    converter: types.ConverterType[typing.Any, var.OutType]

    def build_entry(self) -> types.EntryType[typing.Never, var.OutType]:
        return entries.ImmutableEntry(
            self.key,
            self.reader,
            self.converter,
            self.default,
        )

    def build_view(self) -> types.ViewType[prototype.Prototype, var.InType, var.OutType]:
        return view.ReadOnlyView()
