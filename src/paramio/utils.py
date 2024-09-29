from __future__ import annotations

import collections.abc

from . import _internal, converters, field, types
from ._internal import typing


def _is_classvar(type_: typing.Any) -> bool:
    if type_ is typing.ClassVar:
        return True
    elif (org := typing.get_origin(type_)) is typing.ClassVar:
        return True
    elif org is not typing.Annotated:
        return False

    return _is_classvar(typing.get_origin(typing.get_args(type_)[0]))


def _create_field_builder(
    defaults: field.Params, **params: typing.Unpack[field.Params]
) -> field.FieldBuilder[typing.Any, typing.Any]:
    return field.FieldBuilder(**(defaults | params))


def _fill_field_builder(
    field: field.FieldBuilder[typing.Any, typing.Any],
    **params: typing.Unpack[field.Params],
) -> field.FieldBuilder[typing.Any, typing.Any]:
    for key, value in params.items():
        setattr(field, key, value)
    return field


def _get_field_builders(
    classdict: collections.abc.Mapping[str, typing.Any],
    **kwds: typing.Unpack[field.Params],
) -> dict[str, types.FieldBuilderType[typing.Any, typing.Any, typing.Any]]:
    fields = {}
    for name, type_ in classdict.get("__annotations__", {}).items():
        value = classdict.get(name, _internal.SENTINEL)

        if isinstance(value, types.FieldBuilderType):
            attr = value
        elif hasattr(value, "__get__") or _is_classvar(type_) or isinstance(value, types.ViewType):
            continue
        elif name.startswith("_"):
            continue
        elif name not in classdict:
            attr = _create_field_builder(kwds, key=name, converter=converters.Caster(type_))
        else:
            attr = _create_field_builder(kwds, default=value, key=name, converter=converters.Caster(type_))

        fields[name] = attr

    return fields
