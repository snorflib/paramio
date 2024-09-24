from __future__ import annotations

import abc
import typing

from src.paramio import types

Inst = typing.TypeVar("Inst")
InType = typing.TypeVar("InType", contravariant=True)
OutType = typing.TypeVar("OutType", covariant=True)


class BaseView(types.ViewType[Inst, InType, OutType]):
    __slots__ = ("_name",)

    @typing.overload
    def __get__(self, instance: None, owner: type[Inst]) -> typing.Self: ...
    @typing.overload
    def __get__(self, instance: Inst, owner: type[Inst]) -> OutType: ...
    def __get__(self, instance: Inst | None, owner: type[Inst]) -> OutType | typing.Self:
        if instance is None:
            return self

        return self._get_value(instance, owner)

    def __set__(self, instance: Inst, value: InType) -> None:
        self._set_value(instance, value)

    def __set_name__(self, owner: type[Inst], name: str) -> None:
        self._name = name

    @abc.abstractmethod
    def _get_value(self, instance: Inst, owner: type[Inst]) -> OutType:
        raise NotImplementedError

    @abc.abstractmethod
    def _set_value(self, instance: Inst, value: InType) -> None:
        raise NotImplementedError
