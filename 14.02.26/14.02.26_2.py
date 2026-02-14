def factorial(n): # Для 1 задания
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def first(lessons):
    print(f"Количество комбинаций: {factorial(len(lessons))}")
    print("\nВсе комбинации:")
    result = [[]]
    for i in lessons:
        new_res = []
        for j in result:
            for n in range(len(j) + 1):
                new_res.append(j[:n] + [i] + j[n:])

        result = new_res
    return result


if __name__ == "__main__":
    lessons = ["Физра", "Русский язык", "Алгебра", "Физика", "Информатика"]
    print(first(lessons))