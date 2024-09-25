from __future__ import annotations

import abc
import typing

from src.paramio import types
from src.paramio.types import var

if typing.TYPE_CHECKING:
    import typing_extensions as t_ext


class BaseView(types.ViewType[var.Inst, var.InType, var.OutType]):
    __slots__ = ("_name",)

    @typing.overload
    def __get__(self, instance: None, owner: type[var.Inst]) -> t_ext.Self: ...
    @typing.overload
    def __get__(self, instance: var.Inst, owner: type[var.Inst]) -> var.OutType: ...
    def __get__(self, instance: var.Inst | None, owner: type[var.Inst]) -> var.OutType | t_ext.Self:
        if instance is None:
            return self

        return self._get_value(instance, owner)

    def __set__(self, instance: var.Inst, value: var.InType) -> None:
        self._set_value(instance, value)

    def __set_name__(self, owner: type[var.Inst], name: str) -> None:
        self._name = name

    @abc.abstractmethod
    def _get_value(self, instance: var.Inst, owner: type[var.Inst]) -> var.OutType:
        raise NotImplementedError

    @abc.abstractmethod
    def _set_value(self, instance: var.Inst, value: var.InType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def console_printable(self, instance: var.Inst, owner: type[var.Inst]) -> str:
        raise NotImplementedError
