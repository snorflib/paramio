<div align="center">

# <img src="https://github.com/user-attachments/assets/6e2145a4-3fb5-4f86-8395-d6ebbd3139c4" width="250px"/>

[![License](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
<a href="https://github.com/snorflib/paramio"><img src="https://img.shields.io/github/stars/snorflib/paramio?style=social" alt="Paramio's GitHub repo"></a>

[Advantages](#why-paramio) • [Start](#how-to-start) • [Contributing](#contributing)

</div>

**Paramio** provides an easy-to-use interface for defining, loading, and managing configurations in Python projects. It supports multiple configuration file formats like JSON, YAML, INI, and TOML, offering a declarative syntax for organizing application parameters.

## Why Paramio

🧩 **No External Dependencies**. The library is self-contained and doesn't rely on any third-party packages, ensuring compatibility and reducing the risk of dependency conflicts.

🧙 **Lightweight**. With a minimal footprint, the library adds little overhead to your project, making it ideal for applications where performance and simplicity are key.

🦋 **Easily Extensible**. Designed with flexibility in mind, the library can be easily extended to meet custom requirements. You can effortlessly add new configuration sources or define custom loaders and parsers.

🛠 **Follows Best Practices**. The library is built according to industry best practices, promoting clean, maintainable, and well-organized code. It encourages a clear separation of configuration logic and application logic.

## Version compatibility

| Paramio | Python  | Support |
|---------|---------|---------|
| 1.x.x   | 3.10 >= | ✅ Current 

## How to start

```ssh
// uv
> uv add paramio

// poetry
> poetry add paramio

// pip
> pip install paramio
```

## Example

```python
# Load config from JSON

import paramio


@paramio.paramio(prefix="DB_", reader=paramio.JSON(), case_sensitive=False)
class DataBase:
    password: str | None
    username: str | None
    port: int = 8080
    host: str = paramio.field(default="localhost", prefix="POSTGRES_")

    def get_full_url(self) -> str:
        return f"{self.host}:{self.port}/{self.username}@{self.password}
```

## Contributing

Here's how you can contribute:

- [Open an issue](https://github.com/snorflib/paramio/issues) if you believe you've encountered a bug.
- Make a [pull request](https://github.com/snorflib/paramio/pull) to add new features/make quality-of-life improvements/fix bugs.

<a href="https://github.com/snorflib/paramio/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=snorflib/paramio" />
</a>

## Repo Activity

![Repo Activity](https://repobeats.axiom.co/api/embed/e1b457a7bf51281e0c247aa7195101c8ac950d8b.svg "Repobeats analytics image")

## License

🆓 Feel free to use our library in your commercial and private applications

Package are covered by [MIT Licence](/LICENSE)
