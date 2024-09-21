import typing

ValueType = typing.TypeVar("ValueType")


class EntryType(typing.Protocol[ValueType]):
    value: ValueType
