import typing

from . import _field, types


def is_classvar(type_: typing.Any) -> bool:
    if type_ is typing.ClassVar:
        return True
    elif (org := typing.get_origin(type_)) is typing.ClassVar:
        return True
    elif org is not typing.Annotated:
        return False

    return is_classvar(typing.get_origin(typing.get_args(type_)[0]))


def _create_field(params_high: dict[str, typing.Any], **params_low: dict[str, typing.Any]) -> _field.Field:
    return _field.Field(**(params_low | params_high))


def create_fields_from_cls(cls: type[typing.Any], **kwds: dict[str, typing.Any]) -> dict[str, _field.Field]:
    fields = {}
    for name, type_ in cls.__annotations__.items():
        if (value := getattr(cls, name, None)) is None:
            attr = _create_field(kwds, key=name)
        elif hasattr(value, "__get__") or is_classvar(type_) or isinstance(value, types.ViewType):
            continue
        elif isinstance(value, _field.Field):
            attr = value
        else:
            attr = _create_field(kwds, default=value, key=name)

        fields[name] = attr
    return fields
