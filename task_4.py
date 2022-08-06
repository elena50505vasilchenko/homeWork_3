# 1 способ
def my_func(x, y):
    """Возведение числа в степень без цикла"""
    return x ** y


print(my_func(int(input()), int(input())))


# 2 способ
def my_func_1(x, y):
    """Возведение числа в степень с циклом"""
    res = 1
    for i in range(0, abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(my_func_1(int(input()), int(input())))
