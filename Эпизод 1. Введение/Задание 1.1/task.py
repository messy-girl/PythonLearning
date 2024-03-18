import math

# Пример 1
def task_1(a, d, c):
    z = (c - (d/5) + 321**(1/2)) / (1 + 3 * a)
    return z


# Пример 2
def task_2(a, d, c):
    # TODO
    z = (math.log10(c/3) - d + 25) / (5 * a - 1)
    return z


# Пример 3
def task_3(a, d, c):
    # TODO
    z = (c/2 + math.log(d, math.e) - 35) / (5 * a + 1)
    return z


# Пример 4
def task_4(a, d, c):
    # TODO
    z = (math.tan(c) + d/32) / (a/3 + 1)
    return z


# Пример 5
def task_5(a, d, c):
    # TODO
    z = (c/5 - d + 1) / (c + math.tan(2 * a))
    return z


# Пример 6
def task_6(a, d, c):
    # TODO
    z = ((25 * c) ** (1/2) + d - 3) / (d - a**2 + 1)
    return z


# Пример 7
def task_7(a, d, c):
    # TODO
    z = (5 * math.log10(c) + 3 * d - 32) / (a ** 2 + 1)
    return z


# Пример 8
def task_8(a, d, c):
    # TODO
    z = (c * d - math.log(4 * 3 * a, math.e)) / (c + a - 1)
    return z
