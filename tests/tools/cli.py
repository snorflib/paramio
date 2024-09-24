import sys

from src.paramio import tools


def test_flag_no_value() -> None:
    sys.argv = ["-config"]
    assert tools.get_flag_value("-config") is None


def test_flag_with_value() -> None:
    sys.argv = ["-config", "filename.txt"]
    assert tools.get_flag_value("-config") == "filename.txt"


def test_no_flag() -> None:
    sys.argv = ["-not-the-flag", "filename.txt"]
    assert tools.get_flag_value("-config") is None
