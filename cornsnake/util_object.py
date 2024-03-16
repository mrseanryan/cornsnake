"""
Functions for working with object attributes. The `get_attributes` function retrieves all non-private attributes of an object. The `get_attribute_value` function returns the value of a specific attribute of an object.
"""

def get_attributes(object):
    """
    Get all non-private attributes of an object.

    Args:
    object: The object to retrieve attributes from.

    Returns:
    list: A list of non-private attributes of the object.
    """
    attributes = []
    all_properties = dir(object)
    for prop in all_properties:
        if not prop.startswith('_'):  # skip built-ins
            attributes.append(prop)
    return attributes

def get_attribute_value(object, attribute_name):
    """
    Get the value of a specific attribute of an object.

    Args:
    object: The object to retrieve the attribute value from.
    attribute_name: The name of the attribute to get the value of.

    Returns:
    The value of the specified attribute of the object.
    """
    return getattr(object, attribute_name)
