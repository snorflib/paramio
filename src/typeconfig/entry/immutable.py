import typing

from src.typeconfig import loader as ld

from .base import BaseEntry

ValueType = typing.TypeVar("ValueType")


class ImmutableEntry(BaseEntry[ValueType]):
    __slots__ = ("_loader",)

    def __init__(self, loader: ld.LoaderType[ValueType]) -> None:
        self._loader = loader

    @property
    def value(self) -> ValueType:
        return self._loader()

    @value.setter
    def value(self, value: ValueType) -> None:
        raise NotImplementedError(f"{self!r} is immutable")
