import typing

from .base import ParamioError


class ConverterError(ParamioError): ...


class CastFailedError(ConverterError):
    def __init__(self, cast_to: typing.Any, value: typing.Any, hint: str = "") -> None:
        self._cast_to = cast_to
        self._value = value
        self._hint = hint

    def __str__(self) -> str:
        value = self._value[: min(15, len(self._value) // 2)] + "***"
        hint = "\n\t\t HINT: {self._hint}" if self._hint else ""
        return f"Couldn't cast value {value!r} to the type {self._cast_to!r}.{hint}"
