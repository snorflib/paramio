from __future__ import annotations

import types as btn_types
import typing

from src.paramio import meta

MappingProxyType = btn_types.MappingProxyType


class Paramio(metaclass=meta.ParamioMeta):
    __slots__ = ("__internal__",)
    __internal__: dict[str, typing.Any]

    def __repr__(self) -> str:
        view_values = []
        for name in type(self).__views__:
            if (attr := getattr(type(self), name, None)) is None:
                continue

            view_values.append(f"{name}={attr.console_printable(self, type(self))}")

        return f"{type(self).__name__}({', '.join(view_values)})"
