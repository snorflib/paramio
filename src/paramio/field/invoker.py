import typing

from src.paramio import exceptions as exc

from .base import BaseField, Inst, InType, OutType


class InvokerField(BaseField[Inst, InType, OutType]):
    __slots__ = (
        "_getter",
        "_setter",
    )

    def __init__(
        self,
        getter: typing.Callable[[Inst], OutType],
        setter: typing.Callable[[Inst, InType], None] | None = None,
    ) -> None:
        self._getter = getter
        self._setter = setter

    def _get_value(self, instance: Inst, owner: type[Inst]) -> OutType:
        return self._getter(instance)

    def _set_value(self, instance: Inst, value: InType) -> None:
        if self._setter is None:
            raise exc.ReadOnlyFieldError(instance, self)

        self._setter(instance, value)
