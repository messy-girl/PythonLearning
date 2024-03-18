def task_1(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return str(mid)
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return '-1'

#-----------------------------------

def task_2(a):
    f = 0
    for i in range(2,a-1):
        if a % i != 0:
            f += 1
    if f == 0:
        return True
    else:
        return False



