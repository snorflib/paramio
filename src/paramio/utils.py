from __future__ import annotations

from . import field
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


def _fill_field_builders(
    field: field.FieldBuilder[typing.Any, typing.Any],
    **params: typing.Unpack[field.Params],
) -> field.FieldBuilder[typing.Any, typing.Any]:
    for key, value in params.items():
        setattr(field, key, value)
    return field


def _get_field_builders(
    classdict: dict[str, typing.Any],
) -> dict[str, field.FieldBuilder[typing.Any, typing.Any]]:
    return {}
