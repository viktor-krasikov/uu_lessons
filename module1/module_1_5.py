# example = "Топинамбур"
# print(example.casefold())
# print(example[0])
# print(example[-1])
# print(example[len(example) // 2:])
# print(example[::-1])
# print(example[1::2])


immutable_var = (1, 2.5, 'string', True)
print("Immutable tuple:", immutable_var)

# immutable_var[0] = 10  # ошибка
# значения элементов кортежа нельзя изменить, потому что это такой тип данных неизменяемый

mutable_list = [1, 2.5, 'string', False]

mutable_list[0] = 10
print("Mutable list (after modification):", mutable_list)
