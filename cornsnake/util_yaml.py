import json
from typing import Any, Dict, List, Union

YAMLType = Union[Dict[str, Any], List[Any], str, int, float, bool, None]


def deep_sort(data: YAMLType) -> YAMLType:
    """
    Recursively sort a YAML-like object (dict, list, etc.) by its keys and values.
    - why: for consistenct comparison.

    Args:
        data (YAMLType): The YAML-like object to sort.

    Returns:
        YAMLType: The sorted YAML-like object.
    """
    if isinstance(data, dict):
        return {k: deep_sort(data[k]) for k in sorted(data)}
    elif isinstance(data, list):
        # sort list items by their JSON string representation
        return sorted(
            (deep_sort(x) for x in data), key=lambda v: json.dumps(v, sort_keys=True)
        )
    else:
        return data
