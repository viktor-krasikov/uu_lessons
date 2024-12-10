def apply_all_func(int_list, *functions):
    return {func.__name__: func(int_list) for func in functions}


# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
