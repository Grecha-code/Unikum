import random
import time


def first(list_for_sort):
    print("\nЗадание 1")
    n = len(list_for_sort)
    # Цикл для прохода по списку
    for i in range(n):
        swapped = False
        # Цикл для перемещения элементов списка
        for j in range(0, n - i - 1):
            # Если элементы не на своем месте, меняем их местами
            if list_for_sort[j] > list_for_sort[j + 1]:
                list_for_sort[j], list_for_sort[j + 1] = list_for_sort[j + 1], list_for_sort[j]
                swapped = True
        # Если не было сортировки, оставляем всё как есть
        if not swapped:
            break
    return list_for_sort


def second(N, M, move):
    print("\nЗадание 2")
    matrix = []

    # Цикл для добавления элементов (0, 1, 2...)
    for i in range(N):
        row = list(range(M))
        matrix.append(row)

    # Цикл для сдвига матрицы
    for i in range(M):
        row = matrix[i]
        move_actual = move % 10
        matrix[i] = row[-move_actual:] + row[:-move_actual]

    # Цикл для вывода матрицы
    for row in matrix:
        print(*row)


def third(N, M):
    print("\nЗадание 3")
    matrix = []

    # Цикл для добавления рандомных элементов
    for i in range(N):
        row = [random.randint(1, 100) for i in range(M)]
        matrix.append(row)

    # Цикл для сортировки и вывода матрицы
    for i in range(len(matrix)):
        print(*first(matrix[i]))


def fourth():
    print("\nЗадание 4")
    data = [random.randint(1, 100) for i in range(10)]
    data2 = data.copy()

    # Сортировка перебором
    def find_max_simple():
        max_val = data[0]
        for i in data:
            if i > max_val:
                max_val = i
        return max_val

    # Пузырьковая сортировка
    def find_max_bubble():
        n = len(data2)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data[-1]

    # Вычислетельный эксперемент
    def check():
        start = time.time()
        find_max_simple()
        print(f"Перебор: {time.time() - start:.5f}с")

        start2 = time.time()
        find_max_bubble()
        print(f"Пузырьковая сортировка: {time.time() - start2:.5f}с")

    check()
    print("Вывод: Соритровка перебором быстрее, "
          "\nпотому что она имеет сложность O(n),"
          "\nа пузырьковая O(n ** 2)")


if __name__ == "__main__":
    while True:
        print("\nКонтрольная работа.\nПашков Алексей, ИИ-71. Уровень C")
        choice = int(input("Какое задание хотите проверить?\n"
                           "Введите 0, если хотите выйти"))

        if choice == 0:
            print("Спасибо за проверку!")
            break

        elif choice == 1:
            print(first([92, 5, 12, 3, 14, 16, 121]))
            print("Метод sort() является более быстрым, т.к.\n"
                  "является гибридным алгоритмом, который\n"
                  "во всех случаях имеет сложность O(n log n)")

        elif choice == 2:
            print(second(10, 10, 3))

        elif choice == 3:
            print(third(7, 7))

        elif choice == 4:
            print(fourth())

        else:
            print("Такой задачи нет!")
