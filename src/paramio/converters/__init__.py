__all__ = (
    "Caster",
    "dummy_converter",
)


import typing

from .caster import Caster

ValueType = typing.TypeVar("ValueType")


def dummy_converter(value_type: ValueType) -> ValueType:
    return value_type
