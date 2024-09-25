from __future__ import annotations

import abc
import typing

from . import var

if typing.TYPE_CHECKING:
    import typing_extensions as t_ext


@typing.runtime_checkable
class ViewType(typing.Protocol[var.Inst, var.InType, var.OutType]):
    @typing.overload
    def __get__(self, instance: None, owner: type[var.Inst]) -> t_ext.Self: ...
    @typing.overload
    def __get__(self, instance: var.Inst, owner: type[var.Inst]) -> var.OutType: ...

    @abc.abstractmethod
    def __get__(self, instance: var.Inst | None, owner: type[var.Inst]) -> var.OutType | t_ext.Self:
        raise NotImplementedError

    @abc.abstractmethod
    def __set__(self, instance: var.Inst, value: var.InType) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def console_printable(self, instance: var.Inst, owner: type[var.Inst]) -> str:
        raise NotImplementedError
