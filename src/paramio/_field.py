from __future__ import annotations

import dataclasses

from src.paramio import _internal, types
from src.paramio._internal import typing

OutType = typing.TypeVar("OutType")


@dataclasses.dataclass(slots=True)
class Field:
    default: typing.Any = _internal.SENTINEL
    key: str = ""
    reader: types.ReaderType[str, typing.Any] | None = None
    conv: types.ConverterType[typing.Any, typing.Any] | None = None
    secret: bool = False

    name: str = dataclasses.field(init=False)
    type_: typing.Any = dataclasses.field(init=False)


class FieldParams(typing.TypedDict, total=False):
    prefix: str
    key: str
    reader: types.ReaderType[str, typing.Any] | None
    conv: types.ConverterType[typing.Any, typing.Any] | None
    secret: bool


def field(default: OutType, **kwargs: typing.Unpack[FieldParams]) -> OutType:
    return Field(**kwargs)  # type: ignore
