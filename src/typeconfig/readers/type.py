import abc
import typing

KeyType = typing.TypeVar("KeyType", contravariant=True)
ValueType = typing.TypeVar("ValueType", covariant=True)


class ReaderType(typing.Protocol[KeyType, ValueType]):
    @abc.abstractmethod
    def __getitem__(self, key: KeyType) -> ValueType:
        raise NotImplementedError
