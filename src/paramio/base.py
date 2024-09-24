from __future__ import annotations

import typing

from . import (
    _field,
    converters,
    entries,
    meta,
    readers,
    views,
)
from .types import var


def default_entry_factory(field: _field.Field) -> entries.ImmutableEntry[var.InType, var.OutType]:
    return entries.ImmutableEntry(
        key=field.prefix + (field.key or field.name),
        reader=field.reader or readers.Env(),
        conv=field.conv or converters.Caster(field.type_),
        default=field.default,
    )


def default_view_factory(field: _field.Field) -> views.InvokerView[ParamioBase, var.InType, var.OutType]:
    def getter(instance: ParamioBase, name: str) -> var.OutType:
        return typing.cast(var.OutType, instance.__internal__[name])

    def on_display(value: var.OutType) -> str:  # type: ignore[misc]
        val_str = str(value)
        if field.secret is False:
            return val_str

        return val_str[: min(15, len(val_str) // 2)] + "***"

    return views.InvokerView(getter, None, on_display)


class ParamioBase(
    metaclass=meta.ParamioMeta,
    view_factory=default_view_factory,
    entry_factory=default_entry_factory,
):
    __slots__ = ("__internal__",)
    __internal__: dict[str, typing.Any]

    def __new__(cls: type[typing.Self], *args: typing.Any, **kwargs: typing.Any) -> typing.Self:
        instance = super().__new__(cls, *args, **kwargs)
        instance.__init_internal__()
        return instance

    def asdict(self) -> dict[str, typing.Any]:
        return self.__internal__

    def __eq__(self, other: typing.Any) -> bool:
        return hasattr(other, "__internal__") and (self.__internal__ == other.__internal__)

    def __init_internal__(self) -> None:
        self.__internal__ = {key: entry.get_value() for key, entry in type(self).__entries__.items()}

    def __repr__(self) -> str:
        view_values = []
        for name in type(self).__views__:
            if (attr := getattr(type(self), name, None)) is None:
                continue

            view_values.append(f"{name}={attr.console_printable(self)}")

        return f"{type(self)}({', '.join(view_values)})"
