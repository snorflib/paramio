import abc
import typing

ValueType = typing.TypeVar("ValueType", contravariant=True)
CastType = typing.TypeVar("CastType", covariant=False, contravariant=False)


class ConverterType(typing.Protocol[ValueType, CastType]):
    @abc.abstractmethod
    def __call__(self, value: ValueType, type_: CastType) -> CastType:
        raise NotImplementedError
