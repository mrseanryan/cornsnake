"""
base64 encode/decode utility functions.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_base64.html)
"""

import base64
from typing import Any


def encode_to_base64(binary_content: Any, encoding: str = "utf-8") -> str:
    """Encode binary data (for example that was read from a file in 'rb' mode) into a base64 string."""
    return base64.b64encode(binary_content).decode(encoding=encoding)


def encode_string_to_base64(text: str, encoding: str = "utf-8") -> str:
    """Encode a string into a base64 string."""
    byte_data = text.encode(encoding=encoding)
    return encode_to_base64(binary_content=byte_data)


def decode_base64_to_binary(base64_string: str) -> Any:
    """Decode base64 string to the original binary data."""
    # Remove the data URL prefix if present
    if base64_string.startswith("data:"):  # for example: data:image/jpeg;base64,
        base64_string = base64_string.split(",")[1]

    # Decode the base64 string
    return base64.b64decode(base64_string)


def save_base64_as_binary_file(base64_string: str, output_file_path: str) -> None:
    """Save base64 string as a decoded binary file."""
    original_binary = decode_base64_to_binary(base64_string=base64_string)

    # Write the binary data to a file
    with open(output_file_path, "wb") as file:
        file.write(original_binary)

    print(f"Image saved successfully as {output_file_path}")
