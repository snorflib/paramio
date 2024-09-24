import typing

from src.paramio import types

from . import utils

ValueType = typing.TypeVar("ValueType", contravariant=True)
CastType = typing.TypeVar("CastType", covariant=True)


class Caster(types.ConverterType[ValueType, CastType]):
    __slots__ = ("_cast_to",)

    def __init__(self, cast_to: type[CastType]) -> None:
        self._cast_to = cast_to

    def __call__(self, value: ValueType) -> CastType:
        try:
            return utils.cast_to_type(self._cast_to, value)
        except IndexError as exc:
            raise exc
        except BaseException as exc:
            raise exc
