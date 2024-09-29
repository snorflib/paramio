import os

import pytest

from src.paramio import readers

os.environ["five"] = "5"
os.environ["siX"] = "6"


@pytest.mark.skipif(os.name == "nt", reason="Environment variables are not case sensitivity on windows.")  # type: ignore
def test_env_case_sensitive() -> None:
    env = readers.Env(case_sensitive=True)
    assert env[("five",)] == "5"
    with pytest.raises(KeyError):
        env[("six",)]


def test_env_non_case_sensitive() -> None:
    env = readers.Env(case_sensitive=False)
    assert env[("five",)] == "5"
    assert env[("Six",)] == "6"


def test_env_get() -> None:
    env = readers.Env(case_sensitive=False)
    assert env.get(("name",), None) is None
    assert env.get(("name",), "abracadabra") == "abracadabra"
