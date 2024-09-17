import abc
import typing

ValueType = typing.TypeVar("ValueType", covariant=True)


class LoaderType(typing.Protocol[ValueType]):
    @abc.abstractmethod
    def __call__(self) -> ValueType:
        raise NotImplementedError
