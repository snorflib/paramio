import typing

from src.paramio import types

from .base import ParamioError


class EntryError(ParamioError): ...


class ReadOnlyEntryError(EntryError):
    def __init__(self, inst: types.EntryType[typing.Any, typing.Any]) -> None:
        self._inst = inst

    def __str__(self) -> str:
        return f"Cannot write to the {self._inst!r}."
