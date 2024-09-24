import types as btn_types
import typing

from . import (
    _field,
    _internal,
    _utils,
    base,
    types,
)


class Params(typing.TypedDict, total=False):
    prefix: str
    reader: types.ReaderType[str, typing.Any]
    singleton: bool
    entry_factory: typing.Callable[[_field.Field], types.EntryType[typing.Any, typing.Any]]
    view_factory: typing.Callable[[_field.Field], types.ViewType[typing.Any, typing.Any, typing.Any]]


@typing.overload
def paramio(maybe_cls: type[typing.Any], /, **kwargs: typing.Unpack[Params]) -> type[base.Paramio]: ...


@typing.overload
def paramio(
    maybe_cls: None = None, /, **kwargs: typing.Unpack[Params]
) -> typing.Callable[[type[typing.Any]], type[base.Paramio]]: ...


def paramio(
    maybe_cls: type[typing.Any] | None = None,
    /,
    **kwargs: typing.Unpack[Params],
) -> type[base.Paramio] | typing.Callable[[type[typing.Any]], type[base.Paramio]]:
    def _inner(cls: type[typing.Any]) -> type[base.Paramio]:
        return _builder(
            cls.__name__,
            cls.__mro__,
            dict(cls.__dict__),
            **kwargs,
        )

    return _inner(maybe_cls) if maybe_cls else _inner


def _builder(
    name: str,
    bases: tuple[typing.Any, ...],
    classdict: dict[str, typing.Any],
    **kwargs: typing.Unpack[Params],
) -> type[base.Paramio]:
    entry_factory = kwargs.pop("entry_factory", _utils.default_entry_factory)
    view_factory = kwargs.pop("view_factory", _utils.default_view_factory)
    singleton = kwargs.pop("singleton", False)

    entries: dict[str, types.EntryType[typing.Any, typing.Any]] = {}
    views: dict[str, types.ViewType[base.Paramio, typing.Any, typing.Any]] = {}
    for key, field_ in _utils.create_fields_from_cls_dict(classdict, **kwargs).items():
        entries[key] = entry_factory(field_)
        views[key] = view_factory(field_)

    entries |= classdict.pop("__entries__", {})
    views |= classdict.pop("__views__", {})

    metacls = _internal.SingletonMeta if singleton else type
    new_cls = metacls(
        name,
        bases if base.Paramio in bases else (base.Paramio, *bases),
        {}
        | {"__entries__": btn_types.MappingProxyType(entries)}
        | {"__views__": tuple(views.keys())}
        | classdict
        | views,
    )
    return typing.cast(type[base.Paramio], new_cls)
