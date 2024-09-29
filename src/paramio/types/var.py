__all__ = (
    "InType",
    "OutType",
)


import typing

from . import key

Inst = typing.TypeVar("Inst", contravariant=True)

InType = typing.TypeVar("InType", contravariant=True)
OutType = typing.TypeVar("OutType", covariant=True)

KeyType = typing.TypeVar("KeyType", contravariant=True, bound=key.KeyType)
RawType = typing.TypeVar("RawType", covariant=True)
