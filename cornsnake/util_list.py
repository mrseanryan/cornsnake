"""
Functions for manipulating lists of data. Functions include chunking lists, excluding elements from one list that are present in another, finding the intersection of two lists, and various other list operations.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_list.html)
"""

from typing import Generator
import typing


def chunk(
    list_a: list, CHUNK_SIZE: int, merge_solitary: bool = False
) -> Generator[list, None, None]:
    """
    Function to chunk a list into sublists of size n.

    Args:
    list_a (list): The input list to be chunked.
    n (int): The size of each chunk.
    merge_solitary: If True, then avoid a 'solitary' item in the final chunk, by including it in the penultimate chunk.

    Yields:
    list: Sublists of size n.
    """
    for i in range(0, len(list_a), CHUNK_SIZE):
        list_end = i + CHUNK_SIZE
        if merge_solitary and len(list_a) - list_end == 1:
            list_end += 1
            yield list_a[i:list_end]
            break

        yield list_a[i:list_end]


def excluding(list1: list, list2: list) -> list:
    """
    Function to exclude elements from list1 that are present in list2.

    Args:
    list1 (list): The main list.
    list2 (list): The list of elements to exclude.

    Returns:
    list: List1 with elements excluded.
    """
    return [x for x in list1 if x not in list2]


def intersecting(list1: list, list2: list) -> list:
    """
    Function to find the intersection of two lists.

    Args:
    list1 (list): The first list.
    list2 (list): The second list.

    Returns:
    list: Intersection of list1 and list2.
    """
    return [value for value in list1 if value in list2]


def first_or_none(my_list: list) -> typing.Any | None:
    """Function to return the first element of a list or None if the list is empty."""
    if len(my_list) > 0:
        return my_list[0]
    return None


def flatten(my_list: list) -> list:
    """Function to flatten a list of lists into a single list."""
    return [item for sublist in my_list for item in sublist]


def list_with_first_or_empty(my_list: list) -> list:
    """Function to return a list containing the first element of the input list, or an empty list if the input list is empty."""
    first_or_none_value = first_or_none(my_list)
    if first_or_none_value is None:
        return []
    return [first_or_none_value]


def not_none(my_list: list) -> list:
    """Function to return a list with non-None elements."""
    return list(filter(lambda f: (f is not None), my_list))


def not_none_and_unique(my_list: list) -> list:
    """Function to return a list with unique non-None elements."""
    return list(set(filter(lambda f: (f is not None), my_list)))


def remove_empty_strings(list_of_strings: list[str]) -> list[str]:
    """Function to remove empty strings from a list of strings."""
    parts_filtered = []
    for part in list_of_strings:
        if part and len(part) > 0:
            parts_filtered.append(part)
    return parts_filtered


def strip_strings(list_of_strings: list[str]) -> list[str]:
    """Function to strip leading and trailing whitespace from strings in a list."""
    parts_stripped = []
    for part in list_of_strings:
        parts_stripped.append(part.strip())
    return parts_stripped


def unique(my_list: list) -> list:
    """Function to return a list with unique elements from the input list."""
    return list(set(my_list))
