"""
Reading TOML (ini) files and updating the global config in memory (from config.py).

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_toml.html)
"""

import tomllib
import typing

from . import config
from . import util_dict
from . import util_list
from . import util_object

# ref https://toml.io/en/


def _read_ini_file(path_to_ini: str) -> dict[str, typing.Any]:
    """Read TOML data from a file."""
    try:
        with open(path_to_ini, "rb") as f:
            data = tomllib.load(f)
            return data
    except FileNotFoundError as fileNotFound:
        raise RuntimeError(
            f"The configuration file {path_to_ini} is missing - {str(fileNotFound)}"
        )
        # NO log available yet
    except tomllib.TOMLDecodeError as tomlError:
        raise RuntimeError(
            f"Please check the configuration file {path_to_ini} - {str(tomlError)}"
        )
        # NO log available yet


def read_config_ini_file(path_to_file: str, config_object: typing.Any = config) -> None:
    """Read TOML data from a file and write it to a config object."""
    data = _read_ini_file(path_to_file)
    _write_data_to_config(data, config_object, path_to_file)


def _write_data_to_config(
    data: dict[str, typing.Any], config_object: typing.Any, filename: str
) -> None:
    """Write data from TOML file to the global config object."""
    config_attributes = util_object.get_attributes(config_object)
    data_attributes = util_dict.get_keys(data)

    unexpected_data = util_list.excluding(data_attributes, config_attributes)
    if len(unexpected_data) > 0:
        raise ValueError(
            f"{filename} has unexpected items: [{' '.join(unexpected_data)}] - please review."
        )

    for data_attribute in data_attributes:
        util_object.set_attribute_value(
            config_object, data_attribute, data[data_attribute]
        )
