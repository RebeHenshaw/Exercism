def flatten(iterable: list[list, int]) -> list[int]:
    """Flatten nested lists."""
    flat_list = []
    for item in iterable:
        if type(item) != list:
                if item != None:
                    flat_list.append(item)
        else:
            flat_list.extend(flatten(item))
    return flat_list
