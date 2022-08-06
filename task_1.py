def my_func(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError as err:
        return err


print(my_func(int(input()), int(input())))
