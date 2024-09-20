__all__ = (
    "Caster",
    "ConverterType",
    "dummy_converter",
)


import typing

from .caster import Caster
from .type import ConverterType

ValueType = typing.TypeVar("ValueType")


def dummy_converter(value_type: ValueType) -> ValueType:
    return value_type
