import os


class Env:
    __slots__ = ()

    def __getitem__(self, key: str) -> str:
        return os.environ[key]
