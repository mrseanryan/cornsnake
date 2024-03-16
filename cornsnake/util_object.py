def get_attributes(object):
    attributes = []
    all_properties = dir(object)
    for prop in all_properties:
        if not prop.startswith('_'):  # skip built-ins
            attributes.append(prop)
    return attributes

def get_attribute_value(object, attribute_name):
    return getattr(object, attribute_name)
