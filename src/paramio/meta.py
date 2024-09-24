from __future__ import annotations

import types as btn_types
import typing

from . import _field, _internal, _utils, types


class ParamioMeta(type):
    __entries__: typing.ClassVar[btn_types.MappingProxyType[str, types.EntryType[typing.Any, typing.Any]]]
    __views__: tuple[str, ...]

    def __new__(
        cls: type[ParamioMeta],
        name: str,
        bases: tuple[type[ParamioMeta]],
        classdict: dict[str, typing.Any],
        entry_factory: typing.Callable[
            [_field.Field], types.EntryType[typing.Any, typing.Any]
        ] = _utils.default_entry_factory,
        view_factory: typing.Callable[
            [_field.Field], types.ViewType[ParamioMeta, typing.Any, typing.Any]
        ] = _utils.default_view_factory,
        singleton: bool = False,
        **kwargs: typing.Unpack[_field.FieldParams[typing.Any]],
    ) -> ParamioMeta:
        fields = _utils.create_fields_from_cls_dict(classdict, **kwargs)

        entries, views = {}, {}
        for key, field_ in fields.items():
            field_.__set_name__(type("BLYAT", (), {"__annotations__": classdict.get("__annotations__", {})}), key)  # type: ignore
            entries[key] = entry_factory(field_)
            views[key] = view_factory(field_)

        entries |= classdict.pop("__entries__", {})

        metacls = _internal.SingletonMeta if singleton else type
        new_cls = metacls.__new__(
            cls,
            name,
            bases,
            classdict
            | {"__entries__": btn_types.MappingProxyType(entries)}
            | {"__views__": tuple(views.keys())}
            | views,
        )
        return new_cls
