# Пример 1
def task_1(n):
    # TODO
    i = 2
    x = 1
    while i < 11:
        x += 1/i
        i += 1
    return x


# Пример 2
def task_2(x, n):
    # TODO
    y = 0
    n = 1
    while n < 18:
        y += x/n
        n += 2
    return y


# Пример 3
def task_3(n):
    # TODO
    a = 1
    y = 1
    while a < n + 1:
        y = y * a
        a += 1
    return y


# Пример 4
def task_4(x, n):
    # TODO
    z = 1
    i = 2
    n = 9
    while i <  n + 1:
        z = z * (x + i) / i
        i = i + 1
    return z


# Пример 5
def task_5(x, n):
    # TODO
    y = -3
    i = 1
    while i < 10:
        y += x * i / (i * 2)
        i += 1
    return y


# Пример 6
def task_6(n):
    # TODO
    z = 1
    i = 2
    n = 20
    while i < n + 1:
        z = z * i
        i = i + 2
    return z
