## TensorRT Log Inspector [WIP]

Easily inspect the TensorRT log files. Check out statistics about optimizations, operations during conversion, displayed in various ways: JSON, table in terminal, or plots.

## Developing

This project is built on [rye](https://rye.astral.sh/), make sure rye is available in your $PATH. After cloning, follow these steps to install dependencies and build the wheel:

```bash
rye sync
rye build
```

The wheel will be available inside the `dist/` directory. Install it in a virtualenv by doing:

```
pip install trt_log_inspector-0.1.0-py3-none-any.whl`
```

## License

The TensorRT Log Inspector is open-sourced, licensed under the [MIT License](https://opensource.org/licenses/MIT).
