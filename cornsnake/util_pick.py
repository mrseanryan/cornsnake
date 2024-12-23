"""
Functions for randomly selecting text. The `pick_one_random` function chooses a random text from a list. The `pick_one_by_prompt` function prompts the user to pick a text from a list.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_pick.html)
"""

import random


def pick_one_random(texts: list[str]) -> str:
    """
    Function to pick a random text from a list.

    Args:
    texts (list): A list of texts to choose from.

    Returns:
    str: A randomly selected text from the list.
    """
    if not texts:
        raise RuntimeError("Arg texts is empty")

    return random.choice(texts)


def pick_one_by_prompt(texts: list[str]) -> str:
    """
    Function to prompt the user to pick a text from a list.

    Args:
    texts (list): A list of texts to choose from.

    Returns:
    str: The text selected by the user.
    """
    if not texts:
        raise RuntimeError("Arg texts is empty")

    valid_selection = None
    while not valid_selection:
        print(texts)
        selected = input("Please pick one >>")
        if selected in texts:
            valid_selection = selected
    return valid_selection
