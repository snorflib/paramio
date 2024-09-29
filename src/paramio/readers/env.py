import os
import typing

from src.paramio import types

DefaultType = typing.TypeVar("DefaultType")
WINDOWS: typing.Final[bool] = os.name == "nt"


def _build_data(case_sensitive: bool = False, encoding: str = "utf-8") -> dict[str, str]:
    if not hasattr(os, "environb"):
        return {k.lower(): val for k, val in os.environ.items()}

    data = {}
    for key_bytes, value_bytes in os.environb.items():
        key = key_bytes.decode()
        data[key if case_sensitive else key.lower()] = value_bytes.decode(encoding)

    return data


class Env(types.ReaderType[tuple[str, ...], str]):
    __slots__ = (
        "case_sensitive",
        "encoding",
    )

    def __init__(
        self,
        case_sensitive: bool = False,
        encoding: str = "utf-8",
    ) -> None:
        self.case_sensitive = False if WINDOWS else case_sensitive
        self.encoding = encoding

    def __getitem__(self, key: tuple[str, ...]) -> str:
        key_str = "".join(key)
        data = _build_data(self.case_sensitive, self.encoding)
        return data[key_str if self.case_sensitive else key_str.lower()]

    def get(self, key: tuple[str, ...], default: DefaultType) -> str | DefaultType:
        key_str = "".join(key)
        key_str = key_str if self.case_sensitive else key_str.lower()
        return _build_data(self.case_sensitive, self.encoding).get(key_str, default)

    def __repr__(self) -> str:
        return type(self).__name__
