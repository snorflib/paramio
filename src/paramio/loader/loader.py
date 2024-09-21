import typing

from src.paramio import types

KeyType = typing.TypeVar("KeyType")
ValueType = typing.TypeVar("ValueType", covariant=True)
T = typing.TypeVar("T")


class Loader(types.LoaderType[ValueType]):
    __slots__ = (
        "_key",
        "_reader",
        "_converter",
    )

    def __init__(
        self,
        key: KeyType,
        reader: types.ReaderType[KeyType, T],
        converter: types.ConverterType[T, ValueType],
    ) -> None:
        self._key = key
        self._reader = reader
        self._converter = converter

    def __call__(self) -> ValueType:
        return self._converter(self._reader[self._key])
