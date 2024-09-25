from __future__ import annotations

import typing

from src.paramio import builder, meta
from src.paramio._internal import typing as my_typing


@typing.overload
def paramio(maybe_cls: type[typing.Any], /, **kwargs: my_typing.Unpack[builder.Params]) -> meta.ParamioMeta: ...


@typing.overload
def paramio(
    maybe_cls: None = None, /, **kwargs: my_typing.Unpack[builder.Params]
) -> typing.Callable[[type[typing.Any]], meta.ParamioMeta]: ...


def paramio(
    maybe_cls: type[typing.Any] | None = None,
    /,
    **kwargs: my_typing.Unpack[builder.Params],
) -> meta.ParamioMeta | typing.Callable[[type[typing.Any]], meta.ParamioMeta]:
    def _inner(cls: type[typing.Any]) -> meta.ParamioMeta:
        return builder.cls_builder(
            cls.__name__,
            cls.__mro__,
            dict(cls.__dict__),
            metacls=meta.ParamioMeta,
            **kwargs,
        )

    return _inner(maybe_cls) if maybe_cls else _inner
