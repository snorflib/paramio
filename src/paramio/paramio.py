import typing

from . import _utils, types

Type = typing.TypeVar("Type")


class Params(typing.TypedDict):
    reader: types.ReaderType[str, typing.Any]


@typing.overload
def paramio(mb_cls: type[Type], **kwargs: typing.Unpack[Params]) -> type[Type]: ...


@typing.overload
def paramio(mb_cls: None, **kwargs: typing.Unpack[Params]) -> typing.Callable[[type[Type]], type[Type]]: ...


def paramio(
    mb_cls: type[Type] | None = None,
    **kwargs: typing.Unpack[Params],
) -> type[Type] | typing.Callable[[type[Type]], type[Type]]:
    def _inner(cls: type[Type]) -> type[Type]:
        fields = _utils.create_fields_from_cls(cls)
        print(fields)
        return cls

    return _inner(mb_cls) if mb_cls else _inner
