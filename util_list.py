# import itertools

def chunk(list_a, n):
    for i in range(0, len(list_a), n):
        yield list_a[i:i + n]

def excluding(list1, list2):
    # list1 less list2
    return [x for x in list1 if x not in list2]

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

def unique(my_list):
    return list(set(my_list))
