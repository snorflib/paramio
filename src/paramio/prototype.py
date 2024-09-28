from __future__ import annotations

import types as btn_types
import typing

from . import types

MappingProxy = btn_types.MappingProxyType


class Prototype(typing.Protocol):
    __entries__: typing.ClassVar[MappingProxy[str, types.EntryType[typing.Any, typing.Any]]] = MappingProxy({})
    __views__: typing.ClassVar[tuple[str, ...]] = ()

    __slots__ = ("__internal__",)
    __internal__: dict[str, typing.Any]

    def __init__(self) -> None:
        self.__build_internal__()

    def __build_internal__(self) -> None:
        # For frozen instances
        object.__setattr__(
            self,
            "__internal__",
            {key: entry.get_value() for key, entry in type(self).__entries__.items()},
        )
