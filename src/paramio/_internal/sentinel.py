from __future__ import annotations

import typing


class _SingletonMeta(type):
    _instances: dict[_SingletonMeta, _SingletonMeta] = {}

    def __call__(cls: _SingletonMeta, *args: typing.Any, **kwargs: typing.Any) -> _SingletonMeta:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


@typing.final
class _Sentinel(metaclass=_SingletonMeta):
    def __init_subclass__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.NoReturn:
        raise NotImplementedError(f"{type(self).__name__!r} must not be subclassed.")


SENTINEL: typing.Final[_Sentinel] = _Sentinel()
