def flatten_dict(d, parent_key=''):
    result = {}
    for key, value in d.items():
        new_key = f"{parent_key}.{key}" if parent_key else str(key)
        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key))
        else:
            result[new_key] = value
    return result

data = {
    'a': {
        'b': 1,
        'c': {
            'd': 2,
            'e': 3
        }
    },
    'f': 4
}
flat = flatten_dict(data)
print("Original Dictionary:", data)
print("Flattened Dictionary:", flat)

""" Output
Original Dictionary: {'a': {'b': 1, 'c': {'d': 2, 'e': 3}}, 'f': 4}
Flattened Dictionary: {'a.b': 1, 'a.c.d': 2, 'a.c.e': 3, 'f': 4}
"""