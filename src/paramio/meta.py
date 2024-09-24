from __future__ import annotations

import types as btn_types
import typing

from . import _field, _internal, _utils, types

EntryFactoryType = typing.Callable[[_field.Field], types.EntryType[typing.Any, typing.Any]]
ViewFactoryType = typing.Callable[[_field.Field], types.ViewType["ParamioMeta", typing.Any, typing.Any]]


class ParamioMeta(type):
    __entries__: typing.ClassVar[btn_types.MappingProxyType[str, types.EntryType[typing.Any, typing.Any]]]
    __views__: tuple[str, ...]

    def __new__(
        cls: type[ParamioMeta],
        name: str,
        bases: tuple[type[ParamioMeta]],
        classdict: dict[str, typing.Any],
        entry_factory: EntryFactoryType,
        view_factory: ViewFactoryType,
        singleton: bool = False,
        **kwargs: typing.Unpack[_field.FieldParams[typing.Any]],
    ) -> ParamioMeta:
        fields = _utils.create_fields_from_cls(cls, **kwargs)

        entries, views = {}, {}
        for key, field_ in fields.items():
            entries[key] = entry_factory(field_)
            views[key] = view_factory(field_)

        entries |= classdict.pop("__entries__", {})

        metacls = _internal.SingletonMeta if singleton else type
        new_cls = metacls(
            name,
            bases,
            classdict
            | {"__entries__": btn_types.MappingProxyType(entries), **views}
            | {"__views__": list(views.keys())},
        )
        return typing.cast(ParamioMeta, new_cls)
