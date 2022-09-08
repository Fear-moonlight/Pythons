def digitize(n):
    lst = []
    str_n = str(n)
    for i in str_n:
        lst.append(i)
    lst.reverse()
    return lst
n = 35231
digitize(n)