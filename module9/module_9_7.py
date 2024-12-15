from sympy import isprime


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Простое" if isprime(result) else "Составное")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
