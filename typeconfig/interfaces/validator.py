import abc
import typing

ValueType = typing.TypeVar("ValueType", contravariant=True)


class ValidatorType(typing.Protocol[ValueType]):
    @abc.abstractmethod
    def __call__(self, __value: ValueType) -> None:
        raise NotImplementedError
