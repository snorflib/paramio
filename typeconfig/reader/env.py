import os
import typing


class Env:
    __slots__ = ()

    def __getitem__(self, key: str) -> typing.Any:
        return os.environ[key]
