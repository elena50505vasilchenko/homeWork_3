def my_func(num_1, num_2, num_3):
    lst = [num_1, num_2, num_3]
    lst.sort()
    summa = sum(lst[1:])
    return summa


print(my_func(int(input()), int(input()), int(input())))
