from src.paramio import exceptions, types
from src.paramio.types import var

from . import utils


class Caster(types.ConverterType[var.InType, var.OutType]):
    __slots__ = ("_cast_to",)

    def __init__(self, cast_to: type[var.OutType]) -> None:
        self._cast_to = cast_to

    def __call__(self, value: var.InType) -> var.OutType:
        try:
            return utils.cast_to_type(self._cast_to, value)
        except IndexError as exc:
            raise exceptions.CastFailedError(
                self._cast_to, value, "Perhaps you didn't specify generics correctly?"
            ) from exc
        except BaseException as exc:
            raise exceptions.CastFailedError(self._cast_to, value) from exc
