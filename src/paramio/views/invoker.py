import typing

from src.paramio import exceptions as exc
from src.paramio.types import var

from .base import BaseView


class InvokerView(BaseView[var.Inst, var.InType, var.OutType]):
    __slots__ = ("_getter", "_setter", "on_display")

    def __init__(
        self,
        getter: typing.Callable[[var.Inst, str], var.OutType],
        setter: typing.Callable[[var.Inst, var.InType, str], None] | None = None,
        on_display: typing.Callable[[var.OutType], str] = lambda val: str(val),  # type: ignore[misc]
    ) -> None:
        self._getter = getter
        self._setter = setter
        self.on_display = on_display

    def _get_value(self, instance: var.Inst, owner: type[var.Inst]) -> var.OutType:
        return self._getter(instance, self._name)

    def _set_value(self, instance: var.Inst, value: var.InType) -> None:
        if self._setter is None:
            raise exc.ReadOnlyViewError(instance, self)

        self._setter(instance, value, self._name)

    def console_printable(self, instance: var.Inst, owner: type[var.Inst]) -> str:
        return self.on_display(self.__get__(instance, owner))
