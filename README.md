# OccuSpytial

A package for fast bayesian analysis of spatial occupancy models. OccuSpytial implements
several samplers for the single season site spatial occupancy model using the Intrinsic Conditional Autoregressive (ICAR) model for spatial random effects.

## Usage

For usage examples refer to the project's [documentation](https://occuspytial.readthedocs.io).


## Installation

The package can be installed using [pip](https://pip.pypa.io).

```shell
pip install occuspytial

```

Alternatively, it can be installed from source using [poetry](https://python-poetry.org)

```shell
git clone https://github.com/zoj613/OccuSpytial.git
cd OccuSpytial/
poetry install

```
Note that installing this way requires that `Cython` is installed for a successful build.


## Testing

To run tests after installation, the package `pytest` is required. Simply run
the following line from the terminal in this package's root directory.

```shell
python -m pytest
```

If all tests pass, then you're good to go.


## Licensing

OccuSpytial is free software made available under the BSD License. For details
see the [LICENSE](https://github.com/zoj613/OccuSpytial/blob/master/LICENSE) file.