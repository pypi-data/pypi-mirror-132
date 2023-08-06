# Workstation

![Tests](https://github.com/militu/workstation/actions/workflows/tests.yml/badge.svg)
![Docs](https://github.com/militu/workstation/actions/workflows/documentation.yml/badge.svg)

### 🕮 Documentation

For detailed documentation (todo), please see [here](https://militu.github.io/workstation/)

```shell
pip install workstation
```

### 🪛 Develop

First install workstation

```shell
pyenv install -s 3.8.12
pyenv local 3.8.12
poetry lock
nox -s pre-commit -- install
nox -s pre-commit -- install --hook-type commit-msg
```
