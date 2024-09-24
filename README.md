<div align="center">

# <img src="https://github.com/user-attachments/assets/6e2145a4-3fb5-4f86-8395-d6ebbd3139c4" width="250px"/>

[![License](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
<a href="https://github.com/snorflib/paramio"><img src="https://img.shields.io/github/stars/snorflib/paramio?style=social" alt="Paramio's GitHub repo"></a>

[Advantages](#why-paramio) • [Get Started](#how-to-get-started) • [Contributing](#contributing)

</div>

**Paramio** offers a seamless interface for defining, loading, and validating configurations within Python projects, enhancing both development efficiency and code reliability.

## Why Paramio

🧩 **No External Dependencies**  
Paramio is completely self-contained, so you won't need to juggle any third-party packages. This keeps your project lean and hassle-free.

🧙 **Lightweight and Efficient**  
Paramio focuses solely on configuration management, adding minimal overhead. It's perfect for projects where performance and simplicity are top priorities.

🦋 **Highly Extensible**  
Paramio is designed to be flexible. You can customize every part of the configuration process, from adding new sources to tweaking the class layout—totally up to you!

## Version Compatibility

| Paramio | Python  | Support  |
|---------|---------|----------|
| 0.1.0   | >= 3.10 | ✅ Current |

## How to Get Started

Choose your preferred package manager to install Paramio:

```bash
# Using uv
uv add paramio

# Using poetry
poetry add paramio

# Using pip
pip install paramio
```

## Example

**Environment Variables (`.env`):**

```env
DB_ROLES = ('user', 'root')
DB_POSTGRES_HOST = "1.1.1.127"

# Password is intentionally omitted
```

**Python Configuration:**

```python
import dotenv; dotenv.load_dotenv() # Note: Native `env` parsing is not yet supported :(

from src.paramio import Paramio, field, readers


class DataBase(
    Paramio,  # Alternatively, use the `paramio` decorator or `ParamioMeta` metaclass
    prefix="DB_",
    reader=readers.Env(case_sensitive=False),
):
    roles: tuple[str, ...]
    password: str | None = None
    host: str = field(default="localhost", key="POSTGRES_HOST")

    @property
    def first_role(self) -> str:
        return self.roles[0]


# Capture the current configuration state. This instance remains unaffected by subsequent reader changes.
# To synchronize other instances, initialize the class with `singleton=True`.
config = DataBase()

assert config.roles == ("user", "root")
assert config.password is None
assert config.host == "1.1.1.127"
assert config.first_role == "user"
```

## Contributing

- [Open an issue](https://github.com/snorflib/paramio/issues) if you believe you've encountered a bug.
- Make a [pull request](https://github.com/snorflib/paramio/pull) to add new features/make quality-of-life improvements/fix bugs.

## Repository Activity

![Repo Activity](https://repobeats.axiom.co/api/embed/e1b457a7bf51281e0c247aa7195101c8ac950d8b.svg "Repobeats analytics image")

## License

This project is licensed under the [MIT License](/LICENSE).
