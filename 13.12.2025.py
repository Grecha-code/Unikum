import random
import time

start = time.perf_counter()
def clear(): # Нужно для промота страницы
    qq = input("Нажмите Enter чтобы продолжить, введите 1 чтобы завершить проверку")
    if qq == "1":
        print(f"Время выполнения: {end - start:0.6f} секунд")
        exit()
    for i in range(100):
        print()
    home()


def first(): # Задача 1
    # Генерация списка
    n = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    # Вычисление результата
    for i in range(len(my_list)):
        if my_list[i-1] + my_list[i] >= 0:
            n += 1
    print(f"Количество положительных пар: {n}")
    clear()


def second(): # Задача 2
    # Генерация списка
    max_nums = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    # Вычисление результата
    for i in range(len(my_list)):
        if my_list[i - 1] + my_list[i] >= max_nums:
            max_nums = my_list[i - 1] + my_list[i]
    print(f"Сумма самой большой пары: {max_nums}")
    clear()


def third(): # Задача 3
    # Генерация списка
    n = []
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    # Вычисление результата
    for i in range(len(my_list)):
        if my_list[i-1] < my_list[i] >= 0:
            n.append([my_list[i-1], my_list[i]])
    print(f"Пары, где второй элемент больше первого: {n}")
    clear()


def fourth(): # Задача 4
    # Генерация списка
    n = 0
    my_list = [random.randint(0, 1000) for i in range(20)]
    print(my_list)
    # Вычисление результата
    for i in range(len(my_list)):
        if my_list[i-1] % 2 == 0 and my_list[i] % 2 == 0 and my_list[i+1] % 2 == 0:
            n += 1
    print(f"Количество чётных троек: {n}")
    clear()


def fifth(): # Задача 5
    # Генерация списка
    n = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    # Вычисление результата
    for i in range(len(my_list)):
        if my_list[i-1] + my_list[i] >= 0 and my_list[i-1] + my_list[i] % 7 == 2:
            n += 1
    print(f"Количество пар, дающие остаток 2 при делении на 7: {n}")
    clear()


def sixth(): # Задача 6
    # Генерация списка
    n = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    # Вычисление результата
    for i in range(len(my_list)):
        if my_list[i] != 0:
            condition1 = abs(my_list[i-1] + my_list[i]) > 14
            condition2 = abs(my_list[i-1] / my_list[i]) > 1
            if condition1 and condition2:
                n += 1
    print(f"Количество пар, выполняющие условия задачи: {n}")
    clear()


def home(): # Главная страница
    print("Пашков Алексей, задания на 13.12.2025")
    print("Введите номер проверяемой задачи: ")
    task = int(input())
    # Выбор задачи
    if task == 1:
        first()
    elif task == 2:
        second()
    elif task == 3:
        third()
    elif task == 4:
        fourth()
    elif task == 5:
        fifth()
    elif task == 6:
        sixth()
    else:
        print("Такой задачи нет!")
end = time.perf_counter()
home()

