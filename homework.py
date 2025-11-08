# Задача 1
def one(n):
    for i in range(1, n+1):
        print(i)

# Задача 2
def two():
    A = int(input())
    B = int(input())
    if A < B:
        for i in range(A, B+1):
         print(i)
    elif A == B:
        print(A)
    else:
        for i in range(B, A-1, -1):
            print(i)

# Задача 3
def three(N):
    q = None
    if N % 2 == 0:
        while True:
            if N == 1:
                q = "YES"
                break
            elif N < 1:
                q = "NO"
                break
            N /= 2
    else:
        q = "NO"
    print(q)

# Задача 4
def four(a):
    if a <= 1:
        return a
    return four(a-1) + four(a-2)