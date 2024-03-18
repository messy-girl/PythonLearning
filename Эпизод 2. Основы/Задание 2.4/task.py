def task_1(str):
    # TODO
    letters = {}
    for i in range(len(str)):
        if str[i] not in " .,?!:0123456789":
            if str[i] not in letters:
                letters[str[i]] = 1
            elif str[i] in letters:
                letters[str[i]] += 1
    return letters


def task_2(list):
    # TODO
    numbers = set()
    s = 0
    for i in range(len(list)):
        if list[i] not in numbers:
            numbers.add(list[i])
            s += list[i]

    return s


def task_3(cities):
    # TODO
    line = ''
    for i in range(len(cities)):
        if i + 1 == len(cities):
            line += cities[i] + '.'
        else:
            line += cities[i] + ', '
    return line


def task_4(a, b):
    # TODO
    c = []
    for i1 in range(len(a)):
        for i2 in range(len(b)):
            if a[i1] == b[i2] and a[i1] not in c:
                c.append(a[i1])
    cmin = min(c)
    c[0] = max(c)
    c[1] = cmin
    c[-1] = 7
    return c
