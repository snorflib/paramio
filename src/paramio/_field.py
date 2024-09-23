from __future__ import annotations

import dataclasses
import typing

from . import _internal, base, types

OutType = typing.TypeVar("OutType")


@dataclasses.dataclass(slots=True)
class Field:
    default: typing.Any = _internal.SENTINEL
    prefix: typing.Any | None = None
    key: typing.Any | None = None
    reader: types.ReaderType[typing.Any, typing.Any] | None = None
    conv: types.ConverterType[typing.Any, typing.Any] | None = None

    name: str = dataclasses.field(init=False)
    type_: typing.Any = dataclasses.field(init=False)

    def __set_name__(self, obj: type[base.BaseConfig], name: str) -> None:
        self.type_ = obj.__annotations__.get(name, typing.Any)
        self.name = name


def field(
    default: OutType,
    key: typing.Any,
    reader: types.ReaderType[typing.Any, typing.Any],
    conv: types.ConverterType[typing.Any, OutType],
) -> OutType:
    return Field(**vars())  # type: ignore
