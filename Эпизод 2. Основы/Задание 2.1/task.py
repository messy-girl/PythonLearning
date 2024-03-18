def task_1(N):
    # TODO
    z = 1
    i = 1
    while i <= N:
        z = z * i
        i += 1
    factorial = z
    return z


def task_2(N):
    # TODO
    b = [0, 1]
    df = 1
    for i in range(0, 50):
        df = b[-1]
        df += b[-2]
        b.append(df)
    print(b[N-1])
    return b[N-1]


def task_3(N):
    # TODO
    arraylist = []
    for i in range(1, N + 1):
        if N % i == 0:
           arraylist.append(i)
    sorted(arraylist)
    print(arraylist)
    return arraylist
