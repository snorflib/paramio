import typing

from . import types

Type = typing.TypeVar("Type")


class Params(typing.TypedDict):
    reader: types.ReaderType[str, typing.Any]


@typing.overload
def paramio(mb_cls: type[Type], **kwargs: typing.Never) -> type[Type]: ...


@typing.overload
def paramio(mb_cls: None, **kwargs: typing.Unpack[Params]) -> typing.Callable[[type[Type]], Type]: ...


def paramio(
    mb_cls: type[Type] | None = None, **kwargs: typing.Unpack[Params] | typing.Never
) -> Type | typing.Callable[[type[Type]], Type]:
    return mb_cls
