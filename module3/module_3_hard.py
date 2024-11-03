def sum_of_entries(data_structure):
    result = 0
    if isinstance(data_structure, (int, float)):
        result = data_structure
    elif isinstance(data_structure, str):
        result = len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        result = sum(map(sum_of_entries, data_structure))
    elif isinstance(data_structure, dict):
        result = sum_of_entries(list(data_structure.keys())) + sum_of_entries(list(data_structure.values()))
    # print(f"SUM({data_structure})")
    # print(f" = {result}")
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_of_entries(data_structure)
print(result)
