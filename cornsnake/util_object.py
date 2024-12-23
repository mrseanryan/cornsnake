"""
Functions for working with object attributes. The `get_attributes` function retrieves all non-private attributes of an object. The `get_attribute_value` function returns the value of a specific attribute of an object.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_object.html)
"""

import typing


def get_attributes(object: typing.Any) -> list[str]:
    """
    Dynamically get all non-private attributes of an object (reflection).

    Args:
    object: The object to retrieve attributes from.

    Returns:
    list: A list of non-private attributes of the object.
    """
    attributes = []
    all_properties = dir(object)
    for prop in all_properties:
        if not prop.startswith("_"):  # skip built-ins
            attributes.append(prop)
    return attributes


def get_attribute_value(object: typing.Any, attribute_name: str) -> typing.Any:
    """
    Dynamically get the value of a specific attribute of an object.

    Args:
    object: The object to retrieve the attribute value from.
    attribute_name: The name of the attribute to get the value of.

    Returns:
    The value of the specified attribute of the object.
    """
    return getattr(object, attribute_name)


def set_attribute_value(
    object: typing.Any, attribute_name: str, value: typing.Any
) -> None:
    """Dynamically set the value of the given attribute of that object.

    Args:
    object: The object upon which to set the attribute value.
    attribute_name: The name of the attribute to set the value of.
    """
    setattr(object, attribute_name, value)


def has_attribute(object: typing.Any, attribute_name: str) -> bool:
    """
    Dynamically check if the given object has an attribute with that name (reflection).

    Args:
    object: The object to retrieve attributes from.
    attribute_name: The name of the attribute to find.

    Returns:
    True if that object has an attribute with that name. Else False.
    """
    return attribute_name in get_attributes(object)
