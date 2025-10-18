import random, time
import sys

text_1 = "\rВведите длину территории(10-50): "
text_2 = "\rВведите ширину территории(10-50): "
text_3 = "\rВведите кол-во островов: "
dls = 1

for i in text_1:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)
sys.stdout.write('\n')
sys.stdout.flush()

M = int(input())

for i in text_2:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)

N = int(input())

for i in text_3:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)

qq = int(input())

result = 0

matrix = [['≈']*N for i in range(M)]
result += qq

for i in range(qq):
    f = random.randint(0, M-1)
    g = random.randint(0, N-1)
    matrix[f][g] = '▩'
    for j, d in [(0,1) , (1,0), (0,-1), (-1,0)]:
        if random.random() < 0.4:
            ff = f + j
            jh = d + g
            if 0 <= ff < M and 0 <= jh < N:
                matrix[ff][jh] = '▩'
www = random.randint(0, len(matrix))
matrix[www][www] = '⨉'

print("Карта:")
for i in matrix:
    print(' '.join(i))

print()
print(f"Кол-во островов: {result}")