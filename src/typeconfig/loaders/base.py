import typing

from src.typeconfig import converters, readers

KeyType = typing.TypeVar("KeyType")
ValueType = typing.TypeVar("ValueType", covariant=True)
T = typing.TypeVar("T")


class Loader(typing.Generic[ValueType]):
    __slots__ = (
        "_key",
        "_reader",
        "_converter",
    )

    def __init__(
        self,
        key: KeyType,
        reader: readers.ReaderType[KeyType, T],
        converter: converters.ConverterType[T, ValueType],
    ) -> None:
        self._key = key
        self._reader = reader
        self._converter = converter

    def __call__(self) -> ValueType:
        return self._converter(self._reader[self._key])
