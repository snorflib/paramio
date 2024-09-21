import abc
import typing

InType = typing.TypeVar("InType", contravariant=True)
OutType = typing.TypeVar("OutType", covariant=True)


class EntryType(typing.Protocol[InType, OutType]):
    @abc.abstractmethod
    def get_value(self) -> OutType:
        raise NotImplementedError

    @abc.abstractmethod
    def set_value(self, __value: InType) -> None:
        raise NotImplementedError
