# Ruff complaints when overload is not from the standard library
from typing import overload

from . import prototype, types
from ._internal import typing
from .types import var

Self = typing.TypeVar("Self")
Inst = typing.TypeVar("Inst", bound=prototype.Prototype)


class View(types.ViewType[Inst, var.InType, var.OutType]):
    __slots__ = ("_name",)

    @overload
    def __get__(self, instance: None, owner: type[Inst]) -> typing.Self: ...
    @overload
    def __get__(self, instance: Inst, owner: type[Inst]) -> var.OutType: ...
    def __get__(self, instance: Inst | None, owner: type[Inst]) -> var.OutType | typing.Self:
        if instance is None:
            return self

        return typing.cast(var.OutType, instance.__internal__[self._name])

    def __set__(self, instance: Inst, value: var.InType) -> typing.NoReturn:
        raise NotImplementedError

    def __set_name__(self, owner: type[Inst], name: str) -> None:
        self._name = name
