class CarException(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectVinNumber(CarException):
    pass


class IncorrectCarNumbers(CarException):
    pass


class Car:
    def __init__(self, model, vin, numbers):
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


for params in [('Model1', 1000000, 'f123dj'),
               ('Model2', 300, 'т001тр'),
               ('Model3', 2020202, 'нет номера')]:
    try:
        car = Car(*params)
    except CarException as exc:
        print(exc.message)
    else:
        print(f'{car.model} успешно создан')
