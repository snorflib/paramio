import typing

from src.paramio import exceptions as exc

from .base import BaseView, Inst, InType, OutType


class InvokerView(BaseView[Inst, InType, OutType]):
    __slots__ = (
        "_getter",
        "_setter",
    )

    def __init__(
        self,
        getter: typing.Callable[[Inst, str], OutType],
        setter: typing.Callable[[Inst, InType, str], None] | None = None,
    ) -> None:
        self._getter = getter
        self._setter = setter

    def _get_value(self, instance: Inst, owner: type[Inst]) -> OutType:
        return self._getter(instance, self._name)

    def _set_value(self, instance: Inst, value: InType) -> None:
        if self._setter is None:
            raise exc.ReadOnlyViewError(instance, self)

        self._setter(instance, value, self._name)
