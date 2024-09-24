import os
import typing

from src.paramio import field, paramio


@paramio
class MockEnvConfig:
    ROLES: tuple[str] | str | int
    HOST: typing.Annotated[str, "Looks like it's annotated"]
    PORT: int = 8080
    USERNAMES: list[str] | str = ""
    PASSWORD: str | None = field(default=None, secret=True, prefix="DB_")

    MY_VAR: typing.ClassVar[str] = "This value wouldn't be affected."

    @property
    def URL(self) -> str:
        return f"{self.HOST}:{self.PORT}/{self.USERNAMES}@{self.PASSWORD}"


def test_standard_case() -> None:
    _set_environ(
        to_delete=("PORT",),
        ROLES="('user',)",
        HOST="localhost",
        PASSWORD="what",
        DB_PASSWORD="test123",
        USERNAMES="['abra']",
        MY_VAR="Erm, what the sigma?",
    )

    config = MockEnvConfig()
    assert config.ROLES == ("user",)
    assert config.HOST == "localhost"
    assert config.PORT == 8080
    assert config.USERNAMES == ["abra"]
    assert config.PASSWORD == "test123"
    assert config.MY_VAR == "This value wouldn't be affected."


def _set_environ(to_delete: typing.Iterable[str] | None = None, **kwargs: str) -> None:
    for key, value in kwargs.items():
        os.environ[key] = value

    for key in to_delete or ():
        os.environ.pop(key, None)
