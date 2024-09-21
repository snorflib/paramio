import typing

from src.paramio import types

from .base import ParamioError


class FieldError(ParamioError): ...


class ReadOnlyFieldError(FieldError):
    def __init__(self, inst: types.FieldType[typing.Any, typing.Any, typing.Any]) -> None:
        self._inst = inst

    def __str__(self) -> str:
        return f"{self._inst!r} is read only. And cannot be re-assigned."
