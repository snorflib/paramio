__all__ = (
    "SENTINEL",
    "SingletonMeta",
)

import typing as _typing

from .singleton import SingletonMeta

SENTINEL: _typing.Final[object] = object()
