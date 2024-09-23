import abc
import typing

KeyType = typing.TypeVar("KeyType", contravariant=True)
ValueType = typing.TypeVar("ValueType", covariant=True)
DefaultType = typing.TypeVar("DefaultType")


class ReaderType(typing.Protocol[KeyType, ValueType]):
    @abc.abstractmethod
    def __getitem__(self, key: KeyType) -> ValueType:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, key: KeyType, default: DefaultType) -> ValueType | DefaultType:
        raise NotImplementedError
