def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(2)
print_params(a=2)
print_params(b='стр2')
print_params(c=False)
print_params(a=3, b='стр3')
print_params(b='стр4', a=4)
print_params(5, b='стр5')
print_params(a=6, c=False)
print_params(c=False, a=7)
print_params(8, c=False)
print_params(a=9, b='стр6', c=False)
print_params(b='стр7', a=10, c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [100, 'Тест1', False]
values_dict = {'a': 200, 'b': 'Тест2', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
