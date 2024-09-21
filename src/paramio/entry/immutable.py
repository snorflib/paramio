import typing

from src.paramio import exceptions as exc
from src.paramio import types

from .base import BaseEntry

ValueType = typing.TypeVar("ValueType")


class ImmutableEntry(BaseEntry[ValueType]):
    __slots__ = ("_loader",)

    def __init__(self, loader: types.LoaderType[ValueType]) -> None:
        self._loader = loader

    @property
    def value(self) -> ValueType:
        return self._loader()

    @value.setter
    def value(self, value: typing.Never) -> None:
        raise exc.ReadOnlyEntryError(self)
