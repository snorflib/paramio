import typing

ValueType = typing.TypeVar("ValueType")


class FieldType(typing.Protocol[ValueType]):
    value: ValueType
