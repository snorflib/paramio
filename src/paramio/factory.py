import typing

from . import builder, meta


@typing.overload
def paramio(maybe_cls: type[typing.Any], /, **kwargs: typing.Unpack[builder.Params]) -> meta.ParamioMeta: ...


@typing.overload
def paramio(
    maybe_cls: None = None, /, **kwargs: typing.Unpack[builder.Params]
) -> typing.Callable[[type[typing.Any]], meta.ParamioMeta]: ...


def paramio(
    maybe_cls: type[typing.Any] | None = None,
    /,
    **kwargs: typing.Unpack[builder.Params],
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
