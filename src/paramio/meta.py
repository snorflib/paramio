from __future__ import annotations

import types as btn_types

from src.paramio import builder, types
from src.paramio._internal import typing


class ParamioMeta(type):
    __is_paramio__: typing.ClassVar[bool] = True

    __entries__: btn_types.MappingProxyType[str, types.EntryType[typing.Any, typing.Any]]
    __views__: tuple[str, ...]
    __internal__: dict[str, typing.Any]
    __internal_init__: typing.Callable[[ParamioMeta], None]

    def __new__(
        cls: type[ParamioMeta],
        name: str,
        bases: tuple[type[ParamioMeta]],
        classdict: dict[str, typing.Any],
        **kwargs: typing.Unpack[builder.Params],
    ) -> ParamioMeta:
        return builder.cls_builder(name, bases, classdict, metacls=cls, **kwargs)

    def __call__(self: ParamioMeta, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        instance = super().__call__(*args, **kwargs)
        internal_hook = getattr(instance, "__init_internal__", self._default_init_internal)
        internal_hook(instance)
        return instance

    @staticmethod
    def _default_init_internal(instance: ParamioMeta) -> None:
        instance.__internal__ = {key: entry.get_value() for key, entry in type(instance).__entries__.items()}
