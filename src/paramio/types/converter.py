import abc
import typing

ValueType = typing.TypeVar("ValueType", contravariant=True)
ReturnType = typing.TypeVar("ReturnType", covariant=True)


class ConverterType(typing.Protocol[ValueType, ReturnType]):
    @abc.abstractmethod
    def __call__(self, __value: ValueType) -> ReturnType:
        raise NotImplementedError
