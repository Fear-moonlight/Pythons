def is_square(n):
    root =  n ** (1/2)
    if root ** 2 == n:
        print(True)
    else:
        print(False)

n = -1
is_square(n)

T = n ** (2)
print(type(T))
