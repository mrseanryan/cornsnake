# cornsnake

A small library wrapping common Python utilities for working with files, git, ZIP, lists, processes, dates and times.

Functions that I find myself writing time and again, on various OSS and personal projects - so collecting in one place, in case it is of use!

For more details, see the [documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/).

[url_repo]: https://github.com/mrseanryan/cornsnake
[url_semver_org]: https://semver.org/

[![MIT License][img_license]][url_license]
[![Supported Python Versions][img_pyversions]][url_pyversions]
[![cornsnake][img_version]][url_version]

[![PyPI Releases][img_pypi]][url_pypi]
[![PyPI - Downloads](https://img.shields.io/pypi/dm/cornsnake.svg)](https://pypi.org/project/cornsnake)

[img_license]: https://img.shields.io/badge/License-MIT-blue.svg
[url_license]: https://github.com/mrseanryan/cornsnake/blob/master/LICENSE

[url_version]: https://pypi.org/project/cornsnake/

[img_version]: https://img.shields.io/static/v1.svg?label=SemVer&message=cornsnake&color=blue
[url_version]: https://pypi.org/project/bumpver/

[img_pypi]: https://img.shields.io/badge/PyPI-wheels-green.svg
[url_pypi]: https://pypi.org/project/cornsnake/#files

[img_pyversions]: https://img.shields.io/pypi/pyversions/cornsnake.svg
[url_pyversions]: https://pypi.python.org/pypi/cornsnake

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K73ALBJ)

## Install

```
python -m pip install --upgrade cornsnake
```

## Dependencies

- Python 3.11 or higher

```
pip install PyMuPDF
```

- fitz is for PDF parsing (installed as PyMuPDF)

## Usage

Functions are organised in modules, providing logical groups like `util_file` or `util_print`.

To use a particular module, simply import it from cornsnake:

```python
from cornsnake import util_file, util_print
```

Then, the modules are available to use:

```python
lines = util_file.read_lines_from_file("my-file.txt")
util_print.print_result(f"Read {len(lines)} lines")
```

To see what functions are available, see the [Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/) or [source code](https://github.com/mrseanryan/cornsnake/tree/master/cornsnake).

For examples see the [unit tests](https://github.com/mrseanryan/cornsnake/tree/master/tests/unit) and [e2e tests](https://github.com/mrseanryan/cornsnake/tree/master/tests/e2e).

## Modules

| Module | Description | Documentation |
|---|---|---|
| config | Globally accessible config object. Can be configured by for example reading from command line arguments or TOML file (via tomllib), and then writing to the properties in-memory.\n- see util_toml.py for an example of reading from an ini file (TOML format). | [config docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/config.html) |
| util_color | Defines color constants and a function for colorizing text output for terminal. | [util_color docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_color.html) |
| util_date | Functions for date manipulation. It includes functions to parse, format, add days to, and validate dates in the yyyy-mm-dd format. | [util_date docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_date.html) |
| util_dependencies | Functions for checking the versions of Python and Git. It ensures that the major and minor versions of these dependencies meet the required criteria. | [util_dependencies docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_dependencies.html) |
| util_dir | Working with directories, files, and file paths. | [util_dir docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_dir.html) |
| util_file | File operations including copying, reading, and writing text to files. | [util_file docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_file.html) |
| util_git | Functions for interacting with a Git repository. It includes functions for executing Git commands, checking out branches, handling commits, and managing Git configuration settings. | [util_git docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_git.html) |
| util_input | Functions for handling user input with various formats and validations. | [util_input docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_input.html) |
| util_json | Functions for reading from and writing to a JSON file. The `read_from_json_file` function reads JSON data from a file, and the `write_to_json_file` function writes JSON data to a file. | [util_json docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_json.html) |
| util_list | Functions for manipulating lists of data. Functions include chunking lists, excluding elements from one list that are present in another, finding the intersection of two lists, and various other list operations. | [util_list docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_list.html) |
| util_log | Functions for logging exceptions and setting up logging configurations. | [util_log docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_log.html) |
| util_markdown_table | Generating Markdown content. Functions like adding row separators, generating Markdown images, and generating italicized text are included. | [util_markdown_table docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_markdown_table.html) |
| util_network | Making a POST request using the urllib library. | [util_network docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_network.html) |
| util_object | Functions for working with object attributes. The `get_attributes` function retrieves all non-private attributes of an object. The `get_attribute_value` function returns the value of a specific attribute of an object. | [util_object docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_object.html) |
| util_os | Functions for checking the operating system and logging OS information. The functions determine if the OS is Windows, Mac, or Unix, and log relevant OS details. | [util_os docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_os.html) |
| util_pdf | Functions for extracting text from a PDF file and checking if a file is a PDF. | [util_pdf docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_pdf.html) |
| util_pick | Functions for randomly selecting text. The `pick_one_random` function chooses a random text from a list. The `pick_one_by_prompt` function prompts the user to pick a text from a list. | [util_pick docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_pick.html) |
| util_print | A Single entry point for printing - so can add custom printing with color and logging. Functions for printing with different colors, logging messages, printing sections, and handling warnings. | [util_print docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_print.html) |
| util_proc | Running processes and opening Windows Explorer at a specified directory. | [util_proc docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_proc.html) |
| util_progress | Functions for tracking progress and updating a progress bar. | [util_progress docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_progress.html) |
| util_robust_delete | Functions for recursively deleting directories and their contents. | [util_robust_delete docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_robust_delete.html) |
| util_string | Check if a text string is empty. The `is_empty` function checks if a text string is None or contains only whitespace or a hyphen. | [util_string docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_string.html) |
| util_text | Defines text constant variables - including for line endings. | [util_text docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_text.html) |
| util_toml | Reading TOML (ini) files and updating the global config in memory (from config.py). | [util_toml docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_toml.html) |
| util_validate | Functions for checking and validating configuration settings in the config.py file. | [util_validate docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_validate.html) |
| util_wait | Function for waiting for a specified number of seconds. The `wait_seconds` function pauses the program execution for the specified number of seconds. | [util_wait docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_wait.html) |
| zip_dir | Function for creating a zip archive from a directory. The `create_zip` function creates a zip archive of a specified directory. | [zip_dir docs](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/zip_dir.html) |

## References

- [github repo](https://github.com/mrseanryan/cornsnake)
- [pypi package](https://pypi.org/project/cornsnake/)
- [documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/)
