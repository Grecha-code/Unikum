import time


def create_hanoi(n, start, end, spare):
    global towers, moves
    moves = 0
    qq = {
        start: list(range(n, 0, -1)),
        spare: [],
        end: []
    }
    towers = dict(sorted(qq.items()))

    def print_towers(towers):
        for i, j in towers.items():
            print(f"{i} {j}")

    print("Первоначальное состояние: ")
    print_towers(towers)
    time.sleep(2)
    print("Начинаем вычисления...")
    time.sleep(2)

    def move_disk(from_tower, to_tower):
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)
        print(f"\nПеремещаем диск {disk} с {from_tower} на {to_tower}")

    def hanoi(n, start, end, spare):
        if n == 1:
            move_disk(start, end)
            return

        hanoi(n-1, start, spare, end)
        print_towers(towers)

        move_disk(start, end)
        print_towers(towers)

        hanoi(n-1, spare, end, start)
        print_towers(towers)

    hanoi(n, start, end, spare)

    print("Окончательное состояние: ")
    print_towers(towers)


if __name__ == "__main__":
    n = int(input("Введите количество дисков: "))
    start = int(input("Введите начальный стержень дисков: "))
    end = int(input("Введите конечный стержень дисков: "))
    spare = None
    my_list = [1, 2, 3]
    my_list.remove(start)
    my_list.remove(end)
    for i in range(len(my_list)):
        spare = my_list[i]

    create_hanoi(n, start, end, spare)
