import os
import typing

from src.paramio import types

DefaultType = typing.TypeVar("DefaultType")


class Env(types.ReaderType[str, str]):
    __slots__ = ()

    def __getitem__(self, key: str) -> str:
        return os.environ[key]

    def get(self, key: str, default: DefaultType) -> str | DefaultType:
        return os.environ.get(key, default)

    def __repr__(self) -> str:
        return type(self).__name__
