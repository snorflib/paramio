import os

from src.paramio import types


class Env(types.ReaderType[str, str]):
    __slots__ = ()

    def __getitem__(self, key: str) -> str:
        return os.environ[key]

    def __repr__(self) -> str:
        return type(self).__name__
