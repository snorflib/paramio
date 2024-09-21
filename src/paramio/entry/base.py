import typing

from src.paramio import exceptions as exc
from src.paramio import types

KeyType = typing.TypeVar("KeyType")
InType = typing.TypeVar("InType")
OutType = typing.TypeVar("OutType")
T = typing.TypeVar("T")


class ImmutableEntry(types.EntryType[InType, OutType]):
    __slots__ = (
        "_key",
        "_reader",
        "_conv",
    )

    def __init__(
        self,
        key: KeyType,
        reader: types.ReaderType[KeyType, T],
        converter: types.ConverterType[T, OutType],
    ) -> None:
        self._key = key
        self._reader = reader
        self._conv = converter

    def get_value(self) -> OutType:
        return self._conv(self._reader[self._key])

    def set_value(self, value: InType) -> None:
        raise exc.ReadOnlyEntryError(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}( {self._reader!r}:{self._key} )"
