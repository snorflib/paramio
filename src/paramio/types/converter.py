import abc
import typing

from . import var


class ConverterType(typing.Protocol[var.InType, var.OutType]):
    @abc.abstractmethod
    def __call__(self, __value: var.InType) -> var.OutType:
        raise NotImplementedError
