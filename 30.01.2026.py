import numpy as np


def generate_3d_matrix(size, low=0, high=100):
    return np.random.randint(low, high, (size, size, size))


def find_coordinates(matrix, target):
    coords = np.argwhere(matrix == target)
    return [c for c in coords]


matrix = generate_3d_matrix(5)
result = find_coordinates(matrix, 5)
for i in range(1):
    try:
        print("Координаты числа: ", *result[i])
    except:
        print("Такого числа в матрице нет!")