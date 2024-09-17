from __future__ import annotations

import typing

from typeconfig import interfaces


class ConfigMeta(type):
    _registry: dict[]

    def __init__(
        cls,
        name: str,
        bases: tuple[type[typing.Any], ...],
        namespace: dict[str, typing.Any],
        **kwargs: dict[str, typing.Any],
    ) -> None

    def __new__(
        cls,
        name: str,
        bases: tuple[type[typing.Any], ...],
        namespace: dict[str, typing.Any],
        **kwargs: typing.Required[dict[str, interfaces.LoaderType[typing.Any]]],
    ) -> ConfigMeta:
        return type.__new__(cls, name, bases, namespace)
