''' Задание от Пашкова Алексея на 06.12.2025 '''
import random

print('Задание от Пашкова Алексея на 06.12.2025')


def clear():
    for i in range(100):
        print()


def first():
    result = 0
    N = int(input("Введите количество вводимых чисел: "))
    c26 = 0
    c13 = 0
    c2 = 0
    my_list = [int(input(f"Введите число {i + 1}: ")) for i in range(N)]
    for i in range(N):
        if my_list[i] % 26 == 0:
            c26 += 1
        elif my_list[i] % 13 == 0:
            c13 += 1
        elif my_list[i] % 2 == 0:
            c2 += 1

        result = c26 * (N - 1) + c2 * c13
    print(result)
    input("Нажмите Enter для выхода в меню")
    clear()
    home()


def second():
    result = 0
    N = int(input("Введите количество вводимых чисел: "))
    c62 = 0
    c31 = 0
    c2 = 0
    my_list = [int(input(f"Введите число {i + 1}: ")) for i in range(N)]
    for i in range(N):
        if my_list[i] % 62 == 0:
            c62 += 1
        elif my_list[i] % 31 == 0:
            c31 += 1
        elif my_list[i] % 2 == 0:
            c2 += 1

        result = c62 * (N - 1) + c2 * c31
    print(result)
    input("Нажмите Enter для выхода в меню")
    clear()
    home()


def third():
    result = 0
    my_list = []
    N = int(input())
    for i in range(N):
        result  = [int(input(f"Пара {i+1}, число {j + 1}: ")) for j in range(2)]
        my_list.append(result)
    print(my_list)


def home():
    print('Задание от Пашкова Алексея на 06.12.2025')
    print('Введите номер задания, которое хотите проверить')
    try:
        task = int(input())
        if task >= 1 and task <= 4:
            if task == 1:
                first()
            elif task == 2:
                second()
            elif task == 3:
                third()
            else:
                fourth()
        else:
            print("Такого задания нет!")
            input("Нажмите Enter для выхода в меню")
            clear()
            home()
    except:
        print("Пожалуйста, введите число!")
        input("Нажмите Enter для выхода в меню")
        clear()
        home()
home()