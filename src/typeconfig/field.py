import typing

from src.typeconfig import loaders

ValueType = typing.TypeVar("ValueType")


class Field(typing.Generic[ValueType]):
    __slots__ = ("_loader",)

    def __init__(self, loader: loaders.LoaderType[ValueType]) -> None:
        self._loader = loader
