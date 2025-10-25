import random

print("Пашков Алексей: ИИ-71, Уровень B")

def first():
    print()
    print("Задача 1")
    print("Эта заадча есть в виде файла в репозитории")

def second():
    print()
    print("Задача 2")
    my_list = []
    positive = 0
    negative = 0
    numbers = int(input('Сколько чисел вы хотите ввести?(Если вы хотите завершить введите "123456"): '))
    if numbers <= 0:
        print("+1 хромосома")
    if numbers == 123456:
        numbers = 0
    for i in range(numbers):
        num = int(input(f"Число {i+1}: "))
        my_list.append(num)
    for i in range(len(my_list)):
        if my_list[i] > 0:
            positive += 1
        elif my_list[i] < 0:
            negative += 1
        else:
            positive += 1
    print(f"Положительных: {positive}")
    print(f"Отрицательных: {negative}")

def third():
    print()
    print("Задача 3")
    my_list = []
    result = 0
    numbers = int(input('Сколько чисел вы хотите сгенерировать?: '))
    if numbers <= 0:
        print("+1 хромосома")
    for i in range(numbers):
        num = random.randint(1, 101)
        my_list.append(num)
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0 and my_list[i] % 3 == 0:
            result += 1
    print(f"Вот все числа:", *my_list)
    print(f"Из них {result} нечётные и кратны трём")

while True:
    print()
    print('Какую задачу вы хотите проверить?(Если хотите закончить, напишите "Выход")')
    num = input()
    if num == '1':
        first()
    elif num == '2':
        second()
    elif num == '3':
        third()
    elif num == "Выход":
        print("Спасибо за проверку!")
        break
    else:
        print("Такой задачи нет!")