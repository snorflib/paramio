import typing

ValueType = typing.TypeVar("ValueType", contravariant=True)
CastType = typing.TypeVar("CastType", covariant=True)


class Caster(typing.Generic[ValueType, CastType]):
    __slots__ = ("_cast_to",)

    def __init__(self, cast_to: CastType) -> None:
        self._cast_to = cast_to

    def __call__(self, value: ValueType) -> CastType:
        return self._cast_to(value)  # type: ignore
