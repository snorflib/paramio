from src.paramio import _internal, types
from src.paramio import exceptions as exc
from src.paramio.types import var


class ImmutableEntry(types.EntryType[var.InType, var.OutType]):
    __slots__ = (
        "_key",
        "_reader",
        "_conv",
        "_default",
    )

    def __init__(
        self,
        /,
        key: var.KeyType,
        reader: types.ReaderType[var.KeyType, var.RawType],
        conv: types.ConverterType[var.RawType, var.OutType],
        default: var.OutType = _internal.SENTINEL,  # type: ignore
    ) -> None:
        self._key = key
        self._reader = reader
        self._conv = conv
        self._default = default

    def get_value(self) -> var.OutType:
        try:
            value = self._reader[self._key]
        except BaseException as exc:
            if self._default is _internal.SENTINEL:
                raise exc
            return self._default

        return self._conv(value)

    def set_value(self, value: var.InType) -> None:
        raise exc.ReadOnlyEntryError(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}( {self._reader!r}:{self._key} )"
