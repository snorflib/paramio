import typing

from src.paramio import exceptions as exc
from src.paramio.types import var

from .base import BaseView


class InvokerView(BaseView[var.Inst, var.InType, var.OutType]):
    __slots__ = (
        "_getter",
        "_setter",
    )

    def __init__(
        self,
        getter: typing.Callable[[var.Inst, str], var.OutType],
        setter: typing.Callable[[var.Inst, var.InType, str], None] | None = None,
    ) -> None:
        self._getter = getter
        self._setter = setter

    def _get_value(self, instance: var.Inst, owner: type[var.Inst]) -> var.OutType:
        return self._getter(instance, self._name)

    def _set_value(self, instance: var.Inst, value: var.InType) -> None:
        if self._setter is None:
            raise exc.ReadOnlyViewError(instance, self)

        self._setter(instance, value, self._name)
