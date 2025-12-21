import time

def create_hanoi(n, start, end, spare):
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
        nonlocal moves
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)
        print()
        print(f"Ход номер {moves+1}:")
        print(f"\nПеремещаем диск {disk} с {from_tower} на {to_tower}")
        moves += 1
        print_towers(towers)

    def hanoi(n, start, end, spare):
        if n == 1:
            move_disk(start, end)
            return

        hanoi(n-1, start, spare, end)

        move_disk(start, end)

        hanoi(n-1, spare, end, start)

    hanoi(n, start, end, spare)

    for i in range(3):
        print()
    print("Окончательное состояние: ")
    print_towers(towers)
    print(f"Понадобилось ходов: {moves}")


if __name__ == "__main__":
    n = int(input("Введите количество дисков: "))
    start = int(input("Введите начальный стержень дисков: "))
    end = int(input("Введите конечный стержень дисков: "))
    start_time = time.perf_counter()
    my_list = [1, 2, 3]
    my_list.remove(start)
    my_list.remove(end)
    spare = my_list[0]
    create_hanoi(n, start, end, spare)
    end_time = time.perf_counter()
    print(f"Время выполнения {end_time - start_time - 4: 0.6f} сек")
