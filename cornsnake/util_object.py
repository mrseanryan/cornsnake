"""
Functions for working with object attributes. The `get_attributes` function retrieves all non-private attributes of an object. The `get_attribute_value` function returns the value of a specific attribute of an object.

[Documentation](http://docs.mrseanryan.cornsnake.s3-website-eu-west-1.amazonaws.com/cornsnake/util_object.html)
"""

def get_attributes(object):
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
        if not prop.startswith('_'):  # skip built-ins
            attributes.append(prop)
    return attributes

def get_attribute_value(object, attribute_name):
    """
    Dynamically get the value of a specific attribute of an object.

    Args:
    object: The object to retrieve the attribute value from.
    attribute_name: The name of the attribute to get the value of.

    Returns:
    The value of the specified attribute of the object.
    """
    return getattr(object, attribute_name)

def set_attribute_value(object, attribute_name, value):
    """Dynamically set the value of the given attribute of that object.

    Args:
    object: The object upon which to set the attribute value.
    attribute_name: The name of the attribute to set the value of.
    """
    setattr(object, attribute_name, value)
