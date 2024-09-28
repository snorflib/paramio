from __future__ import annotations

import abc

# Ruff complaints when overload is not from the standard library
from typing import overload

from src.paramio._internal import typing

from . import var


@typing.runtime_checkable
class ViewType(typing.Protocol[var.Inst, var.InType, var.OutType]):
    @overload
    def __get__(self, instance: None, owner: type[var.Inst]) -> typing.Self: ...
    @overload
    def __get__(self, instance: var.Inst, owner: type[var.Inst]) -> var.OutType: ...

    @abc.abstractmethod
    def __get__(self, instance: var.Inst | None, owner: type[var.Inst]) -> var.OutType | typing.Self:
        raise NotImplementedError

    @abc.abstractmethod
    def __set__(self, instance: var.Inst, value: var.InType) -> None:
        raise NotImplementedError
