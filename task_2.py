def my_func(**info):

    for key, value in info.items():
        print("{} - {} |".format(key, value), end=" ")


my_func(Firstname=input(), Lastname=input(), Year=int(input()), City=input(), email=input(), Phone=int(input()))
