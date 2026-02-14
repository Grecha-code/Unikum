def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def second(numbers):
    print(factorial(len(numbers)))


def third(numbers):
    print(factorial(len(numbers) // 2))


def first(numbers):
    print(factorial(len(numbers) // 2))