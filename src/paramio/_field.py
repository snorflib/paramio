import typing
from dataclasses import dataclass

from . import entry, types, view

SENTINEL = object()


@dataclass(slots=True, kw_only=True)
class Field:
    default: typing.Any = SENTINEL
    key: str | None = None

    def build_entry(self) -> types.EntryType[typing.Any, typing.Any]:
        return entry.ImmutableEntry()

    def build_view(self, getter: typing.Callable[[typing.Any], typing.Any]) -> types.ViewType[*((typing.Any,) * 3)]:
        return view.InvokerView(getter)

    def __set_name__(self, obj: type[typing.Any], name: str) -> None:
        self.key = name


T = typing.TypeVar("T")


def field(default: T) -> T:
    return Field(**vars())  # type: ignore
