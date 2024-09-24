from __future__ import annotations

import types as btn_types
import typing

from . import (
    _field,
    _utils,
    types,
)

Type = typing.TypeVar("Type", bound=type)

Entries = dict[str, types.EntryType[typing.Any, typing.Any]]
Views = dict[str, types.ViewType[typing.Any, typing.Any, typing.Any]]


class Params(typing.TypedDict, total=False):
    prefix: str
    reader: types.ReaderType[str, typing.Any]
    singleton: bool
    entry_factory: typing.Callable[[_field.Field], types.EntryType[typing.Any, typing.Any]]
    view_factory: typing.Callable[[_field.Field], types.ViewType[typing.Any, typing.Any, typing.Any]]


def _build_entries_and_views_from_fields(
    classdict: dict[str, typing.Any],
    **kwargs: typing.Unpack[Params],
) -> tuple[Entries, Views]:
    entry_factory = kwargs.pop("entry_factory", _utils.default_entry_factory)
    view_factory = kwargs.pop("view_factory", _utils.default_view_factory)

    entries: Entries = {}
    views: Views = {}
    for key, field_ in _utils.create_fields_from_cls_dict(classdict, **kwargs).items():
        entries[key] = entry_factory(field_)
        views[key] = view_factory(field_)

    entries |= classdict.pop("__entries__", {})
    return entries, views


def _build_new_classdict(
    classdict: dict[str, typing.Any],
    entries: Entries,
    views: Views,
) -> dict[str, typing.Any]:
    return (
        {}
        | classdict
        | {"__views__": tuple(views.keys())}
        | {"__entries__": btn_types.MappingProxyType(entries)}
        | views
    )


def cls_builder(
    name: str,
    bases: tuple[typing.Any, ...],
    classdict: dict[str, typing.Any],
    metacls: type[Type] = type,  # type: ignore
    **kwargs: typing.Unpack[Params],
) -> Type:
    entries, views = _build_entries_and_views_from_fields(classdict, **kwargs)
    new_dct = _build_new_classdict(classdict, entries, views)

    new_cls = type.__new__(
        metacls,
        name,
        bases,
        new_dct,
    )
    return new_cls
