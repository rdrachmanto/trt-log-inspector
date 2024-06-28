## TensorRT Log Inspector [WIP]

Easily inspect the TensorRT log files. Check out statistics about optimizations, operations during conversion, displayed in various ways: JSON, table in terminal, or plots.

## Developing

This project is built on [rye](https://rye.astral.sh/), make sure rye is available in your $PATH. After cloning, install or update the dependencies by syncing:

```bash
rye sync
```
Please make and run tests when developing. Place test files inside the `tests/` directory, and make the `tests/` directory structure follows `src/trt_log_inspector/`. Note below's example where `test_file_helper.py` is under the `tests/utils/`, equivalent to `src/trt_log_inspector/utils/`.

```bash
├── src
│   └── trt_log_inspector
│       ├── core
│       │   └── __init__.py
│       ├── __init__.py
│       └── utils
│           ├── file_helper.py
│           └── __init__.py
└── tests
    ├── core
    └── utils
        └── test_file_helper.py
```

Below is an example command to make the test file, and to run them. Tests are made with [pytest](https://docs.pytest.org/en/8.2.x/index.html):

```bash
touch tests/[test_file_name.py]
rye test
```

Build the package as a wheel to be able to use this package in a script. Below is an example to build the wheel and to install it in a virtualenv. The generated wheel and tar.gz file is available in `dist/`.

```bash
rye build
pip install trt_log_inspector-0.1.0-py3-none-any.whl`
```
## License

The TensorRT Log Inspector is open-sourced, licensed under the [MIT License](https://opensource.org/licenses/MIT).
