def chunk(list_a, n):
    for i in range(0, len(list_a), n):
        yield list_a[i:i + n]

def excluding(list1, list2):
    # list1 less list2
    return [x for x in list1 if x not in list2]

def intersecting(list1, list2):
    return [value for value in list1 if value in list2]

def first_or_none(my_list):
    if (len(my_list) > 0):
        return my_list[0]
    return None

def flatten(my_list):
    return [item for sublist in my_list for item in sublist]

def list_with_first_or_empty(my_list):
    first_or_none_value = first_or_none(my_list)
    if (first_or_none_value is None):
        return []
    return [first_or_none_value]

def not_none_and_unique(my_list):
    return list(set(filter(lambda f: (f is not None), my_list)))

def remove_empty_strings(list_of_strings):
    parts_filtered = []
    for part in list_of_strings:
        if part and len(part) > 0:
            parts_filtered.append(part)
    return parts_filtered

def strip_strings(list_of_strings):
    parts_stripped = []
    for part in list_of_strings:
        parts_stripped.append(part.strip())
    return parts_stripped

def unique(my_list):
    return list(set(my_list))
