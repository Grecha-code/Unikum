def first():
    N = int(input())
    M = int(input())
    matrix = []
    for i in range(N):
        row = list(range(M))
        matrix.append(row)

    for i in range(N):
        matrix[i].reverse()

    for i in range(M):
        print(*[matrix[j][i] for j in range(N)])

def second_third():
    N = int(input())
    M = int(input())
    matrix = []
    for i in range(N):
        row = list(range(M))
        matrix.append(row)

    for i in range(M):
        print(*[matrix[j][i] for j in range(N)])

second_third()