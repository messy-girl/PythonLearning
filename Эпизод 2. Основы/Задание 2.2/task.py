# Пример 1
def task_1(A):
    # TODO
    s = 0
    for i in range(len(A)):
       if A[i] >= 0:
           s += A[i]
    print(s)
    return s


# Пример 2
def task_2(A):
    # TODO
    sr = 0
    for i in range(len(A)):
        sr += A[i]
    sr = sr / len(A)
    return sr


# Пример 3
def task_3(A):
    # TODO
    sr = 0
    s = 0
    for i in range(len(A)):
        sr += A[i]
    sr = sr / len(A)
    for i in range(len(A)):
        s += (A[i] - sr) ** 2
    s = (s / len(A)) ** (1 / 2)
    return s
