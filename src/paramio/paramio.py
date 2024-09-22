import typing

from . import _field, _utils, types

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
    fields = {}
    for name, type_ in mb_cls.__annotations__.items():
        if (value := getattr(mb_cls, name, None)) is None:
            attr = _field.Field()
        elif hasattr(value, "__get__") or _utils.is_classvar(type_) or isinstance(value, types.ViewType):
            continue
        elif isinstance(value, _field.Field):
            attr = value
        else:
            attr = _field.Field(default=value)

        fields[name] = attr

    print(fields)

    return mb_cls
