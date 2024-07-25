# Carla-Interface

This repository provides stub files for the [Carla](https://github.com/carla-simulator/carla) Python interfaces.

## Overview

The stub files in this repository are generated from the official Carla Python API documentation, offering type hints and improved development experience.

## Installation

```shell
carla_version=0.9.15

# install with rye
rye add carla-interface \
  --git https://github.com/MamoruDS/carla-interface \
  --branch $carla_version

# install with pip
pip install git+https://github.com/MamoruDS/carla-interface.git@$carla_version
```

### Build

Ensure you have the necessary dependencies installed.

```shell
# install with rye
rye sync --all-features

# install with pip
pip install -r requirements-dev.lock
```

The stub files can be easily _built_ via a script, or you can explore our CLI [entry point](./src/carla_doc//__main__.py) to customize your own generation.

```shell
# (optional) specify an interpreter
PYTHON_BIN="$(where python)"

# (optional) specify the target version
CARLA_VERSION='0.9.15'

# (optional) specify the output root
# OUTPUT_DIR=

./build.sh
```

### Patches

The official Carla PythonAPI documentation is handcrafted and contains every banana thing you can imagine, which means the stub file generation can fail.

To address this, we have created documentation patches to fix the parts that are difficult to parse. These patches can be found in [doc_pathces](./doc_patches) within branches corresponding to Carla versions.

## Libraries Used

- [pybind11_stubgen](https://github.com/sizmailov/pybind11-stubgen): Used for generating stub files from structs.

- [pyserde](https://github.com/yukinarit/pyserde) + pyyaml: Used for parsing YAML format documentation.
