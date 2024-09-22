import typing
from dataclasses import dataclass

SENTINEL = object()


@dataclass(slots=True, kw_only=True)
class Field:
    default: typing.Any = SENTINEL


T = typing.TypeVar("T")


def field(default: T) -> T:
    return Field(**vars())  # type: ignore
