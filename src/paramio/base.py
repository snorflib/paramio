from __future__ import annotations

import typing

from . import meta


class ParamioBase(metaclass=meta.ParamioMeta):
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

            view_values.append(f"{name}={attr.console_printable(self, type(self))}")

        return f"{type(self).__name__}({', '.join(view_values)})"
