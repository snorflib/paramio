import abc
import typing

InstanceType = typing.TypeVar("InstanceType")
ValueType = typing.TypeVar("ValueType", covariant=True)


class FieldType(typing.Protocol[ValueType]):
    @typing.overload
    def __get__(self, instance: InstanceType, cls: type[InstanceType]) -> typing.Self: ...

    @typing.overload
    def __get__(self, instance: InstanceType, cls: None = None) -> ValueType: ...

    @abc.abstractmethod
    def __get__(self, instance: InstanceType, cls: type[InstanceType] | None = None) -> ValueType | typing.Self:
        raise NotImplementedError
