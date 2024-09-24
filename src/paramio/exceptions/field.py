from src.paramio import types
from src.paramio.types import var

from .base import ParamioError


class ViewError(ParamioError): ...


class ReadOnlyViewError(ViewError):
    def __init__(self, inst: var.Inst, view: types.ViewType[var.Inst, var.InType, var.OutType]) -> None:
        self._inst = inst
        self._view = view

    def __str__(self) -> str:
        return f"{self._view!r} attribute of the {self._inst} object is read only and cannot be re-assigned."
