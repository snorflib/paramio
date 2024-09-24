import os

from src import paramio


class MockMeta(metaclass=paramio.ParamioMeta):
    user: str


class MockSub(paramio.Paramio):
    user: str


@paramio.paramio
class MockDec:
    user: str


@paramio.paramio
class MockDecSub(paramio.Paramio):
    user: str


@paramio.paramio
class MockDecMeta(metaclass=paramio.ParamioMeta):
    user: str


class _MockNone:
    user: str = "not correct"


@paramio.paramio
class MockSubNoneDec(_MockNone):
    user: str


class MockSubNoneMeta(_MockNone, metaclass=paramio.ParamioMeta):
    user: str


class MockSubNoneSub(_MockNone, paramio.Paramio):
    user: str


@paramio.paramio
class MockDecSubDecDec(MockDec):
    user: str


def test_all_creation_methods() -> None:
    os.environ["user"] = "correct"

    classes = [val for name, val in globals().items() if name.startswith("Mock")]
    instances = [cls() for cls in classes]

    assert all(inst.user == "correct" for inst in instances)
