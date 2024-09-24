from __future__ import annotations

import types as btn_types
import typing

from src.paramio import types

MappingProxy = btn_types.MappingProxyType


class BaseConfig:
    __entries__: typing.ClassVar[MappingProxy[str, types.EntryType[typing.Any, typing.Any]]] = MappingProxy({})

    __slots__ = ("__data__",)
    __data__: dict[str, typing.Any]

    def __new__(cls: type[BaseConfig], *args: typing.Any, **kwargs: typing.Any) -> BaseConfig:
        instance = super().__new__(cls, *args, **kwargs)
        instance.__init_data__()
        return instance

    def asdict(self) -> dict[str, typing.Any]:
        return self.__data__

    def __eq__(self, other: typing.Any) -> bool:
        return hasattr(other, "__data__") and (self.__data__ == other.__data__)

    def __init_data__(self) -> None:
        self.__data__ = {key: entry.get_value() for key, entry in type(self).__entries__.items()}
