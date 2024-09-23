import types as btn_types
import typing

from . import _field, _utils, base, types

Type = typing.TypeVar("Type")


EntryFactoryType = typing.Callable[[_field.Field], types.EntryType[typing.Any, typing.Any]]
ViewFactoryType = typing.Callable[[_field.Field], types.ViewType[base.BaseConfig, typing.Any, typing.Any]]


class Params(typing.TypedDict, total=False):
    reader: types.ReaderType[str, typing.Any]
    prefix: typing.Any

    entry_factory: EntryFactoryType
    view_factory: ViewFactoryType


@typing.overload
def paramio(mb_cls: type[Type], /, **kwargs: typing.Unpack[Params]) -> type[base.BaseConfig]: ...


@typing.overload
def paramio(
    mb_cls: None, /, **kwargs: typing.Unpack[Params]
) -> typing.Callable[[type[Type]], type[base.BaseConfig]]: ...


def paramio(
    mb_cls: type[Type] | None = None,
    /,
    **kwargs: typing.Unpack[Params],
) -> type[base.BaseConfig] | typing.Callable[[type[Type]], type[base.BaseConfig]]:
    entry_factory = kwargs.pop("entry_factory", _utils.default_entry_factory)
    view_factory = kwargs.pop("view_factory", _utils.default_view_factory)

    def _inner(cls: type[Type]) -> type[base.BaseConfig]:
        fields = _utils.create_fields_from_cls(cls, **kwargs)

        entries, views = {}, {}
        for key, field in fields.items():
            entries[key] = entry_factory(field)
            views[key] = view_factory(field)

        entries |= cls.__dict__.get("__entries__", {})
        return type(
            cls.__name__,
            (base.BaseConfig, *cls.__mro__[1:]),
            cls.__dict__ | {"__entries__": btn_types.MappingProxyType(entries), **views},
        )

    return _inner(mb_cls) if mb_cls else _inner
