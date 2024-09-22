Type conversion
Aliases
command line interface
nesting
singleton
only declare typevars once
create interface for the KeyType (__add__)

@paramio(path=..., encoding=..., prefix=..., reader=...)
class A:
    __entries__ = {
        "x": Entry(),
    }

    x: int = 3
    a: int = field(default=4)
    z: str = field(default="hello", view=)
    g: ClassVar[int] = int
    f: tuple[int, int] | None = 


@paramio(reader=Env(), prefix="DB")
class DataBase:
    HOST: str
    PORT: int
    PASSWORD: str
