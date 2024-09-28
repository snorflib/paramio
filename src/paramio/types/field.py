import abc
import typing

from . import entry, var, view

DefaultType = typing.TypeVar("DefaultType")


class FieldBuilderType(typing.Protocol[var.Inst, var.InType, var.OutType]):
    @abc.abstractmethod
    def build_entry(self) -> entry.EntryType[var.InType, var.OutType]:
        raise NotImplementedError

    @abc.abstractmethod
    def build_view(self) -> view.ViewType[var.Inst, var.InType, var.OutType]:
        raise NotImplementedError
