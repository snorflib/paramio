import typing

from src.paramio import types

from .base import ParamioError


class ViewError(ParamioError): ...


class ReadOnlyViewError(ViewError):
    def __init__(self, inst: typing.Any, field: types.ViewType[typing.Any, typing.Any, typing.Any]) -> None:
        self._inst = inst
        self._field = field

    def __str__(self) -> str:
        return f"{self._field!r} attribute of the {self._inst} object is read only and cannot be re-assigned."
