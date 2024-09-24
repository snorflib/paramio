import abc
import typing

from . import var

DefaultType = typing.TypeVar("DefaultType")


class ReaderType(typing.Protocol[var.KeyType, var.RawType]):
    @abc.abstractmethod
    def __getitem__(self, key: var.KeyType) -> var.RawType:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, key: var.KeyType, default: DefaultType) -> var.RawType | DefaultType:
        raise NotImplementedError
