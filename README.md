```py
import paramio


@paramio.paramio(prefix="DB_", reader=paramio.JSON())
class DataBase:
    password: str | None
    username: str | None
    port: int = 8080
    host: str = "localhost" = paramio.field(prefix="POSGRE_")

    def get_full_url(self) -> str:
        return f"{self.host}:{self.port}/{self.username}@{self.password}"
```