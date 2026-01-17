my_list = [1, 2, 3, 4, 5, 6]
new_list = my_list.copy()


def first(list_):
    print()
    print("Задание 1")
    print()
    result = 0
    try:
        for i in range(len(list_)):
            if my_list[i] + my_list[i+1] % 2 != 0:
                print(my_list[i-1], my_list[i])
                result += 1
    except:
        print(result)


def second(list_):
    print("Задание 2")
    print()
    result = 0
    try:
        for i in range(len(list_)):
            list_.remove(list_[i-1])
            if i in list_:
                result += 0
            else:
                result += 1
    except:
        print(result)


def third(list_):
    print()
    print("Задание 3")
    print()
    current = [list_[0]]
    all_seqs = []
    for i in range(1, len(list_)):
        if list_[i] > list_[i - 1]:
            current.append(list_[i])
        else:
            all_seqs.append(current)
            current = [list_[i]]

    all_seqs.append(current)

    max_len = 0

    for i in all_seqs:
        if len(i) > max_len:
            max_len = len(i)

    result = []
    for i in all_seqs:
        if len(i) == max_len:
            result.append(i)

    print("Все возрастающие последовательности:", all_seqs)
    print("Максимальная длина:", max_len)
    print("Самые длинные последовательности:", result)


first(my_list)
second(my_list)
third(new_list)