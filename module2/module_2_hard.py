def generate_password(n):
    result = ""
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += f"{i}{j}"
    return result


n = int(input())
print(generate_password(n))
