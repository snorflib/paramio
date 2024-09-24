from typing import Any, Literal, Never, NoReturn, NotRequired, Optional, Required, TypedDict

import pytest

from src.paramio.converter import utils  # type: ignore


def test_cast_to_int() -> None:
    assert utils.cast_to_type(int, "123") == 123


def test_cast_to_float() -> None:
    assert utils.cast_to_type(float, "123.45") == 123.45


def test_cast_to_str() -> None:
    assert utils.cast_to_type(str, 123) == "123"


def test_cast_to_none() -> None:
    assert utils.cast_to_type(type(None), None) is None


def test_cast_to_any() -> None:
    assert utils.cast_to_type(Any, "anything") == "anything"


def test_cast_to_no_return() -> None:
    with pytest.raises(TypeError):
        utils.cast_to_type(NoReturn, "value")


def test_cast_to_never() -> None:
    with pytest.raises(TypeError):
        utils.cast_to_type(Never, "value")


def test_cast_to_list_int() -> None:
    assert utils.cast_to_type(list[int], ["1", "2", "3"]) == [1, 2, 3]


def test_cast_to_tuple_int() -> None:
    assert utils.cast_to_type(tuple[int, ...], ("1", "2", "3")) == (1, 2, 3)


def test_cast_to_set_float() -> None:
    assert utils.cast_to_type(set[float], {"1.1", "2.2"}) == {1.1, 2.2}


def test_cast_to_frozenset_str() -> None:
    assert utils.cast_to_type(frozenset[str], ["a", "b"]) == frozenset({"a", "b"})


def test_cast_to_dict_str_int() -> None:
    assert utils.cast_to_type(dict[str, int], {"a": "1", "b": "2"}) == {"a": 1, "b": 2}


def test_cast_to_literal() -> None:
    assert utils.cast_to_type(Literal["x", "y"], "x") == "x"
    with pytest.raises(TypeError):
        utils.cast_to_type(Literal["x", "y"], "z")


def test_cast_to_union_int_str() -> None:
    assert utils.cast_to_type(int | str, "123") == 123
    assert utils.cast_to_type(int | str, "abc") == "abc"
    assert utils.cast_to_type(str | int, 456) == "456"


def test_cast_to_optional_int() -> None:
    assert utils.cast_to_type(Optional[int], "789") == 789
    assert utils.cast_to_type(Optional[int], None) is None


def test_cast_to_typed_dict() -> None:
    class Point(TypedDict):
        x: int
        y: int

    value = {"x": "10", "y": "20"}
    assert utils.cast_to_type(Point, value) == {"x": 10, "y": 20}


def test_cast_to_typed_dict_missing_key() -> None:
    class Point(TypedDict):
        x: int
        y: int

    value = {"x": "10"}
    with pytest.raises(TypeError):
        utils.cast_to_type(Point, value)


def test_cast_with_string_type() -> None:
    context = {"CustomType": list[int]}
    value = ["1", "2", "3"]
    assert utils.cast_to_type("CustomType", value, context) == [1, 2, 3]


def test_cast_to_tuple_fixed() -> None:
    assert utils.cast_to_type(tuple[int, str, float], ["1", 2, "3.0"]) == (1, "2", 3.0)


def test_cast_to_union_failure() -> None:
    with pytest.raises(TypeError):
        utils.cast_to_type(int | float, "abc")


def test_cast_to_complex_nested() -> None:
    NestedType = list[dict[str, tuple[int, ...]]]
    value = [{"numbers": ("1", "2")}]
    assert utils.cast_to_type(NestedType, value) == [{"numbers": (1, 2)}]


def test_cast_to_annotated() -> None:
    from typing import Annotated

    assert utils.cast_to_type(Annotated[int, "metadata"], "123") == 123


def test_cast_with_not_required() -> None:
    class Data(TypedDict):
        id: Required[int]
        name: NotRequired[str]

    value = {"id": "1"}
    assert utils.cast_to_type(Data, value) == {"id": 1}


def test_cast_to_union_of_literals() -> None:
    Type = Literal["a"] | Literal["b"]
    assert utils.cast_to_type(Type, "a") == "a"
    assert utils.cast_to_type(Type, "b") == "b"
    with pytest.raises(TypeError):
        utils.cast_to_type(Type, "c")


def test_cast_to_union_with_none() -> None:
    Type = int | None
    assert utils.cast_to_type(Type, "123") == 123
    assert utils.cast_to_type(Type, None) is None


def test_cast_with_invalid_literal() -> None:
    with pytest.raises(TypeError):
        utils.cast_to_type(Literal[1, 2, 3], 4)


def test_cast_to_union_of_types() -> None:
    Type = list[int] | tuple[str, ...]
    assert utils.cast_to_type(Type, ["1", "2"]) == [1, 2]
    assert utils.cast_to_type(Type, ("a", "b")) == ("a", "b")


def test_cast_with_invalid_typed_dict() -> None:
    class Data(TypedDict):
        id: int

    value = {"id": "abc"}
    with pytest.raises(ValueError):
        utils.cast_to_type(Data, value)


def test_cast_to_list_of_unions() -> None:
    Type = list[int | str]
    assert utils.cast_to_type(Type, ["1", 2, "3"]) == [1, 2, 3]


def test_cast_to_tuple_with_ellipsis() -> None:
    assert utils.cast_to_type(tuple[int, ...], ("1", "2", "3")) == (1, 2, 3)


def test_cast_to_set_of_unions() -> None:
    Type = set[int | str]
    assert utils.cast_to_type(Type, {"1", 2, "3"}) == {1, 2, 3}


def test_cast_with_empty_list() -> None:
    assert utils.cast_to_type(list[int], []) == []


def test_cast_with_empty_dict() -> None:
    assert utils.cast_to_type(dict[str, int], {}) == {}


def test_cast_with_wrong_type() -> None:
    with pytest.raises(TypeError):
        utils.cast_to_type(int, ["1", "2"])


def test_cast_with_frozenset() -> None:
    assert utils.cast_to_type(frozenset[int], {"1", "2"}) == frozenset({1, 2})


def test_cast_with_nested_unions() -> None:
    Type = list[int | list[str]]
    value = ["1", ["a", "b"], "2"]
    assert utils.cast_to_type(Type, value) == [1, ["a", "b"], 2]


def test_cast_with_required_and_not_required() -> None:
    class Data(TypedDict, total=True):
        a: int
        b: NotRequired[str]

    value = {"a": "1"}
    assert utils.cast_to_type(Data, value) == {"a": 1}
