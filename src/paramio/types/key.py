import abc
import collections.abc

from src.paramio._internal import typing


class KeyType(collections.abc.Sequence[str]):
    @abc.abstractmethod
    def __add__(self, other: typing.Self) -> typing.Self:
        raise NotImplementedError
