import math

# Пример 1
def task_1(a, b):
    # TODO
    if a > b:
        z = (a * b)**(1/2) - 3
    elif a == b:
        z = math.log10(2)
    else:
        z = math.log(a**3 + 1, math.e) / b
    return z


# Пример 2
def task_2(a, b):
    # TODO
    if a < b:
        z = math.tan(a / b) + 1
    elif a == b:
        z = math.tan(-1)
    else:
        z = (a * b - 5)**(1/2) / a
    return z


# Пример 3
def task_3(a, b):
    # TODO
    if a > b:
        z = math.log10(a * b) + 21
    elif a == b:
        z = math.tan(-5)
    else:
        z = math.log(3 * a / b) + 1
    return z


# Пример 4
def task_4(a, b):
    # TODO
    if a > b:
        z = (a * b - 1) ** (1 / 2)
    elif a == b:
        z = math.log10(255)
    else:
        z = math.tan(a - 5) / b
    return z


# Пример 5
def task_5(a, b):
    # TODO
    if a > b:
        z = math.log(a / b, math.e) + 31
    elif a == b:
        z = math.tan(-25)
    else:
        z = math.cos(a * 5 - 1) / a
    return z


# Пример 6
def task_6(a, b):
    # TODO
    if a < b:
        z = (b / a + 1)**(1/2)
    elif a == b:
        z = 25**(1/2)
    else:
        z = math.log10(a**3 - 5) / b
    return z
