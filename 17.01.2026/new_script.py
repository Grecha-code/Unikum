def first():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    all_numbers = sum(matrix, [])
    duplicates = len(all_numbers) - len(set(all_numbers))

    print(duplicates)


def second():
    matrix = [[1, 2, 3], [1, 2, 3], [4, 5, 6]]
    all_numbers = sum(matrix, [])
    print(len(set(all_numbers)))


def third():
    result = 1
    matrix = [[1, 2, 3], [1, 2, 3], [4, 5, 6]]
    for i in range(len(matrix)):
        result = result * matrix[i][i]
    print(result)