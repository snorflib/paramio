# Ruff complaints when overload is not from the standard library
from typing import overload

from src.paramio._internal import typing

from . import field, utils

Type = typing.TypeVar("Type")


@overload
def paramio(maybe_cls: type[Type], /, **kwargs: typing.Unpack[field.Params]) -> type[Type]: ...


@overload
def paramio(
    maybe_cls: None = None, /, **kwargs: typing.Unpack[field.Params]
) -> typing.Callable[[type[Type]], type[Type]]: ...


def paramio(
    maybe_cls: type[Type] | None = None,
    /,
    **kwargs: typing.Any,
) -> type[Type] | typing.Callable[[type[Type]], type[Type]]:
    def inner(cls: type[Type]) -> type[Type]:
        _ = utils._get_field_builders(cls.__dict__, **kwargs)
        return type(cls)(cls.__name__, cls.__mro__, cls.__dict__)  # type: ignore

    return maybe_cls if maybe_cls else inner
