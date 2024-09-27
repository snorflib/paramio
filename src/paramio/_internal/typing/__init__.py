# ruff: noqa: F405
from __future__ import annotations

__all__ = (
    "is_runtime_type",
    # from `typing`
    "Annotated",
    "Any",
    "Callable",
    "ClassVar",
    "Concatenate",
    "Final",
    "ForwardRef",
    "Generic",
    "Literal",
    "Optional",
    "ParamSpec",
    "Protocol",
    "Tuple",
    "Type",
    "TypeVar",
    "TypeVarTuple",
    "Union",
    "AbstractSet",
    "ByteString",
    "Container",
    "ContextManager",
    "Hashable",
    "ItemsView",
    "Iterable",
    "Iterator",
    "KeysView",
    "Mapping",
    "MappingView",
    "MutableMapping",
    "MutableSequence",
    "MutableSet",
    "Sequence",
    "Sized",
    "ValuesView",
    "Awaitable",
    "AsyncIterator",
    "AsyncIterable",
    "Coroutine",
    "Collection",
    "AsyncGenerator",
    "AsyncContextManager",
    "Reversible",
    "SupportsAbs",
    "SupportsBytes",
    "SupportsComplex",
    "SupportsFloat",
    "SupportsIndex",
    "SupportsInt",
    "SupportsRound",
    "ChainMap",
    "Counter",
    "Deque",
    "Dict",
    "DefaultDict",
    "List",
    "OrderedDict",
    "Set",
    "FrozenSet",
    "NamedTuple",
    "TypedDict",
    "Generator",
    "BinaryIO",
    "IO",
    "Match",
    "Pattern",
    "TextIO",
    "AnyStr",
    "assert_type",
    "assert_never",
    "cast",
    "clear_overloads",
    "dataclass_transform",
    "final",
    "get_args",
    "get_origin",
    "get_overloads",
    "get_type_hints",
    "is_typeddict",
    "LiteralString",
    "Never",
    "NewType",
    "no_type_check",
    "no_type_check_decorator",
    "NoReturn",
    "NotRequired",
    "overload",
    "override",
    "ParamSpecArgs",
    "ParamSpecKwargs",
    "Required",
    "reveal_type",
    "runtime_checkable",
    "Self",
    "Text",
    "TYPE_CHECKING",
    "TypeAlias",
    "TypeGuard",
    "TypeAliasType",
    "Unpack",
)

import types
import typing
from typing import TYPE_CHECKING, Annotated, Any, NoReturn, TypeVar

if TYPE_CHECKING:
    from typing import *  # noqa: F403

    from typing_extensions import Never, NotRequired, Required, Self, Unpack  # noqa: F403

try:
    import typing_extensions
except ImportError:
    typing_extensions = types.ModuleType("typing_extensions")

T = TypeVar("T", bound=Any)
_NotRuntime = Annotated[T, ("__runtime__", False)]
_Fallback: dict[str, typing.Any] = {
    "Never": _NotRuntime[NoReturn],  # type: ignore
    "Self": _NotRuntime[typing.Any],  # type: ignore
    "NotRequired": _NotRuntime,
    "Required": _NotRuntime,
    "Unpack": _NotRuntime,
}

def __getattr__(name: str) -> Any:
    if hasattr(typing, name):
        return getattr(typing, name)
    if hasattr(typing_extensions, name):
        return getattr(typing_extensions, name)

    if name in _Fallback:
        return _Fallback[name]

    raise ImportError(f"cannot import name {name!r} from 'typing' (or 'typing_extensions')")


def is_runtime_type(type: Any) -> bool:
    if typing.get_origin(type) is not typing.Annotated:
        return True
    if not (metadata := type.__metadata__):
        return True
    if not isinstance(data := metadata[0], tuple):
        return True

    return data != ("__runtime__", False)
