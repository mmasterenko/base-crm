def transform_values(iterable, transform):
    if isinstance(iterable, dict):
        iterable = iterable.items()
    return {key: transform(value) for key, value in iterable}


def reverse_dict(dictionary):
    return {v: k for k, v in dictionary.items()}
