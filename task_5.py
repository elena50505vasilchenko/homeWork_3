def my_func():
    summa = 0
    while True:
        num = input().split()
        for i in num:
            try:
                if i == '#':
                    print(summa)
                    return
                else:
                    summa += int(i)
            except ValueError:
                print('err')
            print(summa)


my_func()
