import ast
import types
import typing

CastType = typing.TypeVar("CastType")

if typing.TYPE_CHECKING:
    import typing_extensions as t_ext

def _bool_convert(value: typing.Any) -> bool:
    if isinstance(value, str):
        if (value := value.lower().strip()) == "true":
            return True
        elif value == "false":
            return False
    elif isinstance(value, bool):
        return value

    raise TypeError(f"Cannot convert {value!r} to {bool}.")


def _none_convert(value: typing.Any) -> None:
    if value is None:
        return value
    elif isinstance(value, str) and (value.lower().strip() == "none"):
        return None

    raise TypeError(f"Cannot convert {value!r} to {types.NoneType}.")


def _tuple_convert(value: typing.Any) -> tuple[typing.Any, ...]:
    if isinstance(value, tuple):
        return value
    elif isinstance(value, str):
        return tuple(ast.literal_eval(value))

    return tuple(value)


def _list_convert(value: typing.Any) -> list[typing.Any]:
    if isinstance(value, list):
        return value
    elif isinstance(value, str):
        return list(ast.literal_eval(value))

    return list(value)


def _set_convert(value: typing.Any) -> set[typing.Any]:
    if isinstance(value, set):
        return value
    elif isinstance(value, str):
        return set(ast.literal_eval(value))

    return set(value)


def _frozenset_convert(value: typing.Any) -> frozenset[typing.Any]:
    if isinstance(value, frozenset):
        return value
    elif isinstance(value, str):
        return frozenset(ast.literal_eval(value))

    return frozenset(value)


def _dict_convert(value: typing.Any) -> dict[typing.Any, typing.Any]:
    if isinstance(value, dict):
        return value
    elif isinstance(value, str):
        return dict(ast.literal_eval(value))

    return dict(value)


BuiltInPrimitives: typing.Final[dict[type[typing.Any], typing.Callable[[typing.Any], typing.Any]]] = {
    int: int,
    float: float,
    bool: _bool_convert,
    str: str,
    complex: complex,
    bytes: bytes,
    None: _none_convert,  # type: ignore
}


def _get_type_from_string(type_: str, context: dict[str, typing.Any] | None = None) -> typing.Any:
    try:
        return eval(type_, context or (globals() | locals()))
    except NameError as exc:
        raise ValueError("Couldn't interpret string type, make sure to pass your encapsulated context.") from exc


def _remove_annotated(type_: typing.Any) -> typing.Any:
    if type_ is typing.Annotated:
        return t_ext.Never
    elif typing.get_origin(type_) is typing.Annotated:
        return _remove_annotated(typing.get_args(type_)[0])
    return type_


def cast_to_type(
    type_: type[CastType] | typing.Any,
    value: typing.Any,
    context: dict[str, typing.Any] | None = None,
) -> CastType | typing.Any:
    if type_ is types.NoneType:
        type_ = None
    elif type_ is typing.Any:
        return value
    elif (type_ is t_ext.Never) or (type_ is typing.NoReturn):
        raise TypeError(f"{value!r} cannot be casted to a bottom type.")
    elif isinstance(type_, str):
        type_ = _get_type_from_string(type_, context)
    type_ = _remove_annotated(type_)

    if type_ in BuiltInPrimitives:
        return BuiltInPrimitives[type_](value)

    if isinstance(type_, typing._TypedDictMeta):  # type: ignore
        dict_value = cast_to_type(dict[typing.Any, typing.Any], value)

        for key, val_type in type_.__annotations__.items():
            origin = _remove_annotated(typing.get_origin(val_type))
            args = typing.get_args(val_type)

            must_have = type_.__total__
            if origin is t_ext.NotRequired:
                val_type = args[0]
                must_have = False
            elif origin is t_ext.Required:
                val_type = args[0]
                must_have = True

            if key in dict_value:
                dict_value[key] = cast_to_type(val_type, dict_value[key])
            elif must_have:
                raise TypeError(f"{value!r} does not implement the required key {key!r}.")
        return dict_value

    args = typing.get_args(type_)
    origin = typing.get_origin(type_) or type_

    if origin is typing.ClassVar:
        return cast_to_type(args[0], value)

    if origin is tuple:
        tuple_values = _tuple_convert(value)
        if (args[-1] is Ellipsis) or (args[-1] is types.EllipsisType):
            return tuple(cast_to_type(args[0], val) for val in tuple_values)
        if len(args) != len(tuple_values):
            raise TypeError(f"Cannot cast {len(tuple_values)} values to a tuple with {len(args)} values.")
        return tuple(cast_to_type(t, val) for t, val in zip(args, tuple_values, strict=True))

    if origin is list:
        return [cast_to_type(args[0], val) for val in _list_convert(value)]

    if origin is set:
        return {cast_to_type(args[0], val) for val in _set_convert(value)}

    if origin is dict:
        return {cast_to_type(args[0], key): cast_to_type(args[1], value) for key, value in _dict_convert(value).items()}

    if origin is frozenset:
        return frozenset(cast_to_type(args[0], val) for val in _frozenset_convert(value))

    if origin is typing.Literal:
        if not any(literal == value for literal in args):
            raise TypeError(f"{value!r} does not satisfy any literal {args}")
        return value

    if origin in (typing.Union, types.UnionType):
        for cast_type in args:
            try:
                return cast_to_type(cast_type, value)
            except BaseException:
                continue
        else:
            raise TypeError(f"None of the cast types in `{type_!r}` satisfied the value {value!r}")

    try:
        if isinstance(value, origin):
            return value
    except BaseException:
        ...

    raise TypeError(f"Couldn't cast {value!r} to type `{type_!r}`")
