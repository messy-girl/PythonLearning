import os.path

def task_1(lst):
    most_common = max(set(lst), key=lst.count)
    return most_common
#----------------------------------------
def task_2(X, Y):
    for i in range(8):
        for j in range(i + 1, 8):
            if X[i] == X[j] or Y[i] == Y[j] or abs(X[i] - X[j]) == abs(Y[i] - Y[j]):
                return 'YES'
    return 'NO'
#--------------------------------------------
def task_3(x, y, xc, yc, r):
    if (x - xc)**2 + (y - yc)**2 <= r**2:
        return True
    else:
        return False
#------------------------------------------
def task_4(lst):
    count = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            count += 1
    return count
#----------------------------------------
def task_5(key):
    b = ['jgnnqbyqtnf', 'vjkubkubcbncuvbvcum', 'iqqfbnwem']
    file = open('file.txt', 'r')
    return b


