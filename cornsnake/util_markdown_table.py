"""
Generating Markdown content. Functions like adding row separators, generating Markdown images, and generating italicized text are included.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_markdown_table.html)
"""

MARKDOWN_COLUMN_SEPARATOR = "|"
MARKDOWN_COLUMN_INDICATOR = "---"

def add_row_separator(column_count):
    """
    Function to add row separators for a Markdown table.

    Args:
    column_count (int): The number of columns in the table.

    Returns:
    str: The row separator string for the table.
    """
    row = MARKDOWN_COLUMN_SEPARATOR
    while column_count > 0:
        row += MARKDOWN_COLUMN_INDICATOR + MARKDOWN_COLUMN_SEPARATOR
        column_count -= 1
    return row

def generate_markdown_image(path_to_image, caption):
    """
    Function to generate Markdown image syntax.

    Args:
    path_to_image (str): The path to the image file.
    caption (str): The caption for the image.

    Returns:
    str: The Markdown image syntax.
    """
    return f"![{caption}]({path_to_image} \"{caption}\" )"

def generate_italicised(text):
    """
    Function to generate italicized text in Markdown.

    Args:
    text (str): The text to be italicized.

    Returns:
    str: The italicized text.
    """
    return f"*{text}*"
