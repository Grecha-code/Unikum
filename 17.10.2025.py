import time
import random
import sys
import os

def animate(text = input(), delay=0.2):
    while True:
        string = ""
        for i in text:
            string += i
            sys.stdout.write(f"\r{string}")
            if string == "Def":
                time.sleep(1)
            sys.stdout.flush()
            time.sleep(delay)
        time.sleep(0.5)
        os.system('cls')
        time.sleep(0.5)
        print()

def generate():
    matrix = []
    l = int(input("Введите длину: "))
    h = int(input("Введите ширину: "))
    for j in range(h):
        for i in range(l):
            matrix.append(random.randint(0, 1))
        print(*matrix)
        matrix.clear()
generate()