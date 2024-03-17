"""
Check if a text string is empty. The `is_empty` function checks if a text string is None or contains only whitespace or a hyphen.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_string.html)
"""

def is_empty(text):
    """
    Function to check if a text string is empty or '-'.

    Args:
    text (str): The text string to check.

    Returns:
    bool: True if the text is empty (None or contains only whitespace or a hyphen), False otherwise.
    """
    if text is None:
        return True
    stripped = text.strip()
    return stripped == '' or stripped == '-'
