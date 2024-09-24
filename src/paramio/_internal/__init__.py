__all__ = (
    "SENTINEL",
    "SingletonMeta",
)

import typing

from .singleton import SingletonMeta

SENTINEL: typing.Final[object] = object()
