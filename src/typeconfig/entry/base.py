import abc
import typing

from src.typeconfig import types

ValueType = typing.TypeVar("ValueType")


class BaseEntry(typing.Generic[ValueType], abc.ABC):
    def __init__(self, loader: types.LoaderType[ValueType]) -> None:
        self._loader = loader

    @property
    @abc.abstractmethod
    def value(self) -> ValueType:
        raise NotImplementedError

    @value.setter
    @abc.abstractmethod
    def value(self, value: ValueType) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{type(self)} -> {self.__orig_bases__[0]}"  # type: ignore
