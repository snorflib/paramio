import abc
import typing

from . import var


class EntryType(typing.Protocol[var.InType, var.OutType]):
    @abc.abstractmethod
    def get_value(self) -> var.OutType:
        raise NotImplementedError

    @abc.abstractmethod
    def set_value(self, __value: var.InType) -> None:
        raise NotImplementedError
