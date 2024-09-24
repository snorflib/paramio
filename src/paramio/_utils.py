from __future__ import annotations

import typing

from . import (
    _field,
    converters,
    entries,
    readers,
    types,
    views,
)
from .types import var


def _is_classvar(type_: typing.Any) -> bool:
    if type_ is typing.ClassVar:
        return True
    elif (org := typing.get_origin(type_)) is typing.ClassVar:
        return True
    elif org is not typing.Annotated:
        return False

    return _is_classvar(typing.get_origin(typing.get_args(type_)[0]))


def _create_field(params_high: dict[str, typing.Any], **params_low: typing.Any) -> _field.Field:
    return _field.Field(**(params_high | params_low))


def create_fields_from_cls_dict(
    classdict: dict[str, typing.Any],
    **kwds: typing.Any,
) -> dict[str, _field.Field]:
    fields = {}
    for name, type_ in classdict.get("__annotations__", {}).items():
        private = name.startswith("_")

        if (value := classdict.get(name, None)) is None:
            if private:
                continue
            attr = _create_field(kwds, key=name, conv=converters.Caster(type_))
        elif hasattr(value, "__get__") or _is_classvar(type_) or isinstance(value, types.ViewType):
            continue
        elif isinstance(value, _field.Field):
            attr = value
        elif private:
            continue
        else:
            attr = _create_field(kwds, default=value, key=name, conv=converters.Caster(type_))

        attr.name = name
        attr.type_ = type_

        fields[name] = attr
    return fields


def default_entry_factory(field: _field.Field) -> entries.ImmutableEntry[typing.Any, var.OutType]:
    return entries.ImmutableEntry(
        key=field.prefix + (field.key or field.name),
        reader=field.reader or readers.Env(),
        conv=field.conv or converters.Caster(field.type_),
        default=field.default,
    )


def default_view_factory(field: _field.Field) -> views.InvokerView[typing.Any, var.InType, var.OutType]:
    def getter(instance: typing.Any, name: str) -> var.OutType:
        return typing.cast(var.OutType, instance.__internal__[name])

    def on_display(value: var.OutType) -> str:  # type: ignore[misc]
        cast_to_str = True
        if not isinstance(value, str):
            cast_to_str = False
            value = str(value)  # type: ignore
        if field.secret is True:
            length = len(value)  # type: ignore
            left = min(5, length // 3)
            right = max(length - 5, length - (length // 3))
            value = value[:left] + "..." + value[right:]  # type: ignore
        if cast_to_str:
            return f'"{value}"'
        return str(value)

    return views.InvokerView(getter, None, on_display)
