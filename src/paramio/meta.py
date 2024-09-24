from __future__ import annotations

import types as btn_types
import typing

from . import builder, types


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
        try:
            instance.__init_internal__()
        except AttributeError:
            instance.__internal__ = {key: entry.get_value() for key, entry in self.__entries__.items()}

        return instance
