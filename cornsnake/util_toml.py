"""
Reading TOML (ini) files and updating the global config in memory (from config.py).

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_toml.html)
"""
import tomllib
import sys

from . import config
from . import util_list
from . import util_object
from . import util_print

# ref https://toml.io/en/

def _read_ini_file(path_to_ini):
    """Read TOML data from a file."""
    success = False
    try:
        with open(path_to_ini, "rb") as f:
            data = tomllib.load(f)
            success = True
            return data
    except FileNotFoundError as fileNotFound:
        util_print.print_error(f'The configuration file {path_to_ini} is missing - {str(fileNotFound)}')
        # NO log available yet
    except tomllib.TOMLDecodeError as tomlError:
        util_print.print_error(f'Please check the configuration file {path_to_ini} - {str(tomlError)}')
        # NO log available yet
    finally:
        if not success:
            sys.exit(101)

def read_config_ini_file(path_to_file):
    """Read TOML data from a file and write it to a config object."""
    data = _read_ini_file(path_to_file)
    _write_data_to_config(data, config, path_to_file)

def _write_data_to_config(data, config_object, filename):
    """Write data from TOML file to the global config object."""
    config_attributes = util_object.get_attributes(config_object)
    data_attributes = data.keys()

    unexpected_data = util_list.except_for(data_attributes, config_attributes)
    if len(unexpected_data) > 0:
        raise ValueError(f"{filename} has unexpected items: [{' '.join(unexpected_data)}] - please review.")

    for data_attribute in data_attributes:
        util_object.set_attribute_value(config_object, data_attribute, data[data_attribute])
