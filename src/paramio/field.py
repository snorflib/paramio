import typing
from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class Field:
    default: typing.Any


T = typing.TypeVar("T")


def field(default: T) -> T:
    return Field(**vars())  # type: ignore
