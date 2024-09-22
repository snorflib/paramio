from __future__ import annotations

import dataclasses
import typing

from . import _internal, base, types

KeyType = typing.TypeVar("KeyType", default=typing.Any)
RawType = typing.TypeVar("RawType", default=typing.Any)
OutType = typing.TypeVar("OutType", default=typing.Any)
InType = typing.TypeVar("InType", default=typing.Any)
ConfigType = typing.TypeVar("ConfigType", bound=base.BaseConfig, default=base.BaseConfig)


@dataclasses.dataclass(slots=True)
class Field(
    typing.Generic[
        KeyType,
        RawType,
        InType,
        OutType,
        ConfigType,
    ]
):
    default: OutType | _internal.SentinelType = _internal.SENTINEL
    prefix: KeyType | None = None
    key: KeyType | None = None
    reader: types.ReaderType[KeyType, RawType] | None = None
    conv: types.ConverterType[RawType, OutType] | None = None

    name: str = dataclasses.field(init=False)
    type_: typing.Any = dataclasses.field(init=False)

    def __set_name__(self, obj: type[ConfigType], name: str) -> None:
        self.type_ = obj.__annotations__.get(name, typing.Any)
        self.name = name


def field(
    default: OutType,
    key: KeyType,
    reader: types.ReaderType[KeyType, RawType],
    conv: types.ConverterType[RawType, OutType],
) -> OutType:
    return Field(**vars())  # type: ignore
