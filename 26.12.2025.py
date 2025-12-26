# Начальный список (комментарии оставлены лично Пашковым Алексеем самостоятельно!!! Только для справки)
list_for_sort = [19, 5, 7, 8, 72, 6, 43, 15, 21, 16]
qq = []

# Паста первого списка
for i in range(len(list_for_sort)):
    qq.append(list_for_sort[i-1])

print(f"Список для работы: {qq}")
# Функции
def sort_list(array): # Сортировка длz заданий 1 и 2
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

result = list_for_sort


def first(array): # Задание 1
    array.remove(array[-1])
    print(array[-1])


def second(array): # Задание 2
    array.remove(array[-1])
    array.remove(array[-1])
    print(array[-1])


def third(array): # Задание 3
    result = 0
    for i in range(len(array)):
        if i != 1:
            if array[i - 1] > array[i] and array[i - 1] > array[i + 1]:
                result += 1
    print(result)

def home():  # Главная страница
    sort_list(list_for_sort)
    print("Задание 1:")
    first(list_for_sort)
    input("Нажмите Enter для продолжения")
    print("Задание 2:")
    second(list_for_sort)
    input("Нажмите Enter для продолжения")
    print("Задание 3:")
    third(qq)

home()