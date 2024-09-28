from __future__ import annotations

import dataclasses
import typing

from . import entries, prototype, types, views
from .types import var


@dataclasses.dataclass(slots=True)
class FieldBuilder(
    types.FieldBuilderType[prototype.Prototype, var.InType, var.OutType],
    typing.Generic[var.InType, var.OutType, var.RawType, var.KeyType],
):
    name: str
    key: var.KeyType
    default: var.OutType
    reader: types.ReaderType[var.KeyType, var.RawType]
    converter: types.ConverterType[var.RawType, var.OutType]

    def build_entry(self) -> types.EntryType[var.InType, var.OutType]:
        return entries.ImmutableEntry(
            self.key,
            self.reader,
            self.converter,
            self.default,
        )

    def build_view(self) -> types.ViewType[prototype.Prototype, var.InType, var.OutType]:
        return views.ReadOnlyView()
