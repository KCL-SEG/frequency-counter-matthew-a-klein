"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def is_string(item):
    return isinstance(item, str)

def make_string(item):
    if is_string(item):
        pass
    else:
        item = str(item)
    return item

def frequencies(items):
    frequencies = {}
    string_items = []

    for item in items:

         string_item = make_string(items)
         string_items.append(string_item)

    for string_item in string_items:
        if string_item in frequencies.keys():
            pass
        else:
            frequencies[string_item] = string_items.count(string_item)


    return frequencies
