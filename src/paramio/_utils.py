import typing

from . import _field, converters, types


def _is_classvar(type_: typing.Any) -> bool:
    if type_ is typing.ClassVar:
        return True
    elif (org := typing.get_origin(type_)) is typing.ClassVar:
        return True
    elif org is not typing.Annotated:
        return False

    return _is_classvar(typing.get_origin(typing.get_args(type_)[0]))


def _create_field(params_high: dict[str, typing.Any], **params_low: typing.Any) -> _field.Field:
    return _field.Field(**(params_high | params_low))


def create_fields_from_cls(cls: type[typing.Any], **kwds: typing.Any) -> dict[str, _field.Field]:
    fields = {}
    for name, type_ in cls.__annotations__.items():
        if (value := getattr(cls, name, None)) is None:
            attr = _create_field(kwds, key=name, conv=converters.Caster(type_))
        elif hasattr(value, "__get__") or _is_classvar(type_) or isinstance(value, types.ViewType):
            continue
        elif isinstance(value, _field.Field):
            attr = value
        else:
            attr = _create_field(kwds, default=value, key=name, conv=converters.Caster(type_))

        fields[name] = attr
    return fields
