from __future__ import annotations

import dataclasses
import typing

from . import (
    _internal,
    types,
)

if typing.TYPE_CHECKING:
    import typing_extensions as t_ext

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


def field(default: OutType, **kwargs: t_ext.Unpack[FieldParams]) -> OutType:
    return Field(**kwargs)  # type: ignore
