from __future__ import annotations

import dataclasses
import typing

from . import (
    _internal,
    types,
)

OutType = typing.TypeVar("OutType")


class FieldParams(typing.Generic[OutType], typing.TypedDict, total=False):
    default: OutType
    prefix: str
    key: str
    reader: types.ReaderType[str, typing.Any] | None
    conv: types.ConverterType[typing.Any, typing.Any] | None
    secret: bool


@dataclasses.dataclass(slots=True)
class Field:
    default: typing.Any = _internal.SENTINEL
    prefix: str = ""
    key: str = ""
    reader: types.ReaderType[str, typing.Any] | None = None
    conv: types.ConverterType[typing.Any, typing.Any] | None = None
    secret: bool = False

    name: str = dataclasses.field(init=False)
    type_: typing.Any = dataclasses.field(init=False)


def field(**kwargs: typing.Unpack[FieldParams[OutType]]) -> OutType:
    return Field(**kwargs)  # type: ignore
