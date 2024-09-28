# Ruff complaints when overload is not from the standard library
from typing import overload

from src.paramio._internal import typing

Type = typing.TypeVar("Type")


class Params(typing.TypedDict, total=False): ...


@overload
def paramio(maybe_cls: type[Type], /, **kwargs: typing.Unpack[Params]) -> type[Type]: ...


@overload
def paramio(
    maybe_cls: None = None, /, **kwargs: typing.Unpack[Params]
) -> typing.Callable[[type[Type]], type[Type]]: ...


def paramio(
    maybe_cls: type[Type] | None = None,
    /,
    **kwargs: typing.Any,
) -> type[Type] | typing.Callable[[type[Type]], type[Type]]:
    return maybe_cls if maybe_cls else lambda t: t
