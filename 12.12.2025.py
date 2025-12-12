import random
import time

start = time.perf_counter()
def way_1():
    n = int(input('Введите кол-во чисел в списке: '))
    my_list = [random.randint(1, 17) for i in range(n)]
    my_list.sort()
    print(my_list)
    K = int(input())
    my_list.append(K)
    my_list.sort()
    print(my_list)


def way_3():
    n = int(input('Введите кол-во чисел в списке: '))
    data = [random.randint(1, 17) for i in range(n)]
    data.sort()
    low = 0
    high = len(data) - 1
    middle = (low + high) // 2
    K = int(input())
    while low <= high:
        if data[middle] == K:
            return middle
        elif data[middle] > K:
            high = middle - 1
        else:
            low = middle + 1
    print(data)

def way_4():
    n = int(input('Введите кол-во чисел в списке: '))
    my_list = [random.randint(1, 17) for i in range(n)]
    my_list.sort()
    print(my_list)
    K = int(input())
    my_list.append(K)
    for i in my_list:
        if my_list == my_list.sort():
            break
        else:
            if i == K:
                element = my_list.pop(i)
                my_list.insert(len(my_list), element)
    print(my_list)

end = time.perf_counter()
print(f"Время выполнения: {end-start:0.4f} секунд")