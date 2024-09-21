from __future__ import annotations

import abc
import typing

Inst = typing.TypeVar("Inst", contravariant=True)
InType = typing.TypeVar("InType", contravariant=True)
OutType = typing.TypeVar("OutType", covariant=True)


class FieldType(typing.Protocol[Inst, InType, OutType]):
    @typing.overload
    def __get__(self, instance: None, owner: type[Inst]) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: Inst, owner: type[Inst]) -> OutType: ...

    @abc.abstractmethod
    def __get__(self, instance: Inst | None, owner: type[Inst]) -> OutType | typing.Self:
        raise NotImplementedError

    @abc.abstractmethod
    def __set__(self, instance: Inst, value: InType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def info(self) -> str:
        raise NotImplementedError
