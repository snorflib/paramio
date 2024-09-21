from __future__ import annotations

import typing

Inst = typing.TypeVar("Inst")
InType = typing.TypeVar("InType", contravariant=True)
OutType = typing.TypeVar("OutType", covariant=True)


class FieldType(typing.Protocol[InType, OutType]):
    @typing.overload
    def __get__(self, instance: None, owner: type[Inst]) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: Inst, owner: type[Inst]) -> OutType: ...
    def __get__(self, instance: Inst | None, owner: type[Inst]) -> OutType | typing.Self:
        raise NotImplementedError

    def __set__(self, instance: Inst, value: InType) -> None:
        raise NotImplementedError

    def value_attr_name(self) -> str | None:
        raise NotImplementedError

    def info(self) -> str:
        raise NotImplementedError
