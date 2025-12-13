import random
import time

start = time.perf_counter()
def clear():
    input("Нажмите Enter чтобы продолжить")
    for i in range(100):
        print()
    home()


def first():
    n = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i-1] + my_list[i] >= 0:
            n += 1
    print(f"Количество положительных пар: {n}")
    clear()


def second():
    max_nums = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i - 1] + my_list[i] >= max_nums:
            max_nums = my_list[i - 1] + my_list[i]
    print(f"Сумма самой большой пары: {max_nums}")
    clear()


def third():
    n = []
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i-1] < my_list[i] >= 0:
            n.append([my_list[i-1], my_list[i]])
    print(f"Пары, где второй элемент больше первого: {n}")
    clear()


def fourth():
    n = 0
    my_list = [random.randint(0, 1000) for i in range(20)]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i-1] % 2 == 0 and my_list[i] % 2 == 0 and my_list[i+1] % 2 == 0:
            n += 1
    print(f"Количество чётных троек: {n}")
    clear()


def fifth():
    n = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i-1] + my_list[i] >= 0 and my_list[i-1] + my_list[i] % 7 == 2:
            n += 1
    print(f"Количество пар, дающие остаток 2 при делении на 7: {n}")
    clear()


def sixth():
    n = 0
    my_list = [random.randint(-100, 100) for i in range(20)]
    print(my_list)
    for i in range(len(my_list)):
        if my_list[i] != 0:
            condition1 = abs(my_list[i-1] + my_list[i]) > 14
            condition2 = abs(my_list[i-1] / my_list[i]) > 1
            if condition1 and condition2:
                n += 1
    print(f"Количество пар, выполняющие условия задачи: {n}")
    clear()


def home():
    print("Пашков Алексей, задания на 13.12.2025")
    print("Введите номер проверяемой задачи: ")
    task = int(input())
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

home()
end = time.perf_counter()

print(f"Время выполнения: {end - start:0.6f} секунд")
