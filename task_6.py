def int_func(n):
    """Решение со словами"""
    count = 0
    for i in n:
        num = ord(i)

        if num <= 97 or num >= 122:
            count += 1
            break
    if count > 0:
        return "err"
    else:
        return n.title()


print(int_func(input()))


def int_func_1(n):
    """Решение со строками"""
    count = 0
    a = "".join(n)
    for i in a:
        num = ord(i)

        if num <= 97 or num >= 122:
            count += 1
            break
    if count > 0:
        return "err"
    else:
        str_1 = " ".join(n)
        return str_1.title()


print(int_func_1(input().split()))
