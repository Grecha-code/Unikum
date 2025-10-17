# Задача 1

def one():
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                print(1, end=' ')
            elif i + j > n - 1:
                print(2, end=' ')
            else:
                print(0, end=' ')
        print()

# Задача 2

def two():
    n = int(input())
    gg = list(range(n))
    qq = list(range(n))
    qq.reverse()
    my_list = [*qq[0:-1], *gg]

    first = n
    second = 0

    for i in range(n):
        print(my_list[first:second])
        first -= 1
        second -= 1

# Задача 3

def three():
    n = int(input())
    m = int(input())
    sim_1 = '.'
    sim_2 = '*'
    my_list = []
    your_list = []

    for i in range(n):
        my_list.append(sim_1)
        your_list.append(sim_2)
    for i in range(m):
        print(my_list)
        print(your_list)

# Задача 4

def four():
    n = int(input())
    if n % 2 == 0:
        while True:
            print('Введите число заново! Оно не должно быть чётным')
    for i in range(n):
        matrix = []
        for j in range(n):
            if i == n // 2 or j == n // 2 or i == j or i + j == n - 1:
                matrix.append("*")
            else:
                matrix.append(".")
        print(matrix)

# Задача 5

def five():
    import random
    n = int(input())
    m = int(input())
    max_num = None
    max_i = 0
    max_j = 0

    for i in range(n):
        matrix = []

        for q in range(n):
            matrix.append(random.randint(1, 9))

        for j in range(m):
            if max_num is None or matrix[i] > max_num:
                max_num = matrix[j]
                max_j = j
                max_i = i
    print(max_i, max_j)
def print_figure(matrix):
    for i in matrix:
        print(' '.join(i))
    print()

# Фигуры
def square(size):
    return [['#' for _ in range(size)] for _ in range(size)]

def triangle(size):
    matrix = []
    for i in range(size):
        qq = ['#'] * (i + 1) + [' '] * (size - i - 1)
        matrix.append(qq)
    return matrix

def circle(size):
    matrix = []
    radius = size // 2
    for i in range(size):
        ff = []
        for j in range(size):
            distance = ((i - radius) ** 2 + (j - radius) ** 2) ** 0.5
            if distance <= radius:
                ff.append('#')
            else:
                ff.append(' ')
        matrix.append(ff)
    return matrix

while True:
    print("ВЫБЕРИТЕ ФИГУРУ:")
    print("1 - Квадрат")
    print("2 - Треугольник")
    print("3 - Круг")
    print("4 - Закончить")

    figure = input("Выбор (1-4): ")
    if figure == '4':
        break
    size = int(input("Размер фигуры: "))

    if figure == '1':
        print("Квадрат:")
        print_figure(square(size))
    elif figure == '2':
        print("Треугольник:")
        print_figure(triangle(size))
    elif figure == '3':
        print("Круг:")
        print_figure(circle(size))
    else:
        print("Неверный ввод!")
