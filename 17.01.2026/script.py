def first():
    matrix = []
    move = 1
    for i in range(10):
        row = list(range(10))
        matrix.append(row)

    for i in range(10):
        row = matrix[i]
        move_actual = move % 10
        matrix[i] = row[-move_actual:] + row[:-move_actual]

    for row in matrix:
        print(*row)


def second():
    matrix = []
    move = 1
    for i in range(10):
        row = list(range(10))
        matrix.append(row)

    for i in range(10):
        row = matrix[i]
        move_actual = move % 10
        matrix[i] = row[move_actual:] + row[:move_actual]

    for row in matrix:
        print(*row)


def third():
    matrix = []
    move = int(input())
    for i in range(10):
        row = list(range(10))
        matrix.append(row)

    for i in range(10):
        row = matrix[i]
        move_actual = move % 10
        matrix[i] = row[-move_actual:] + row[:-move_actual]

    for row in matrix:
        print(*row)