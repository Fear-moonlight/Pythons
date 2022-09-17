# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# rules:

#     You need to round the answer to 2 decimal places and return it as String.

#     If the given value is 0 then it should return 0.00

#     You will only be given Natural Numbers as arguments.

n = 3
list_s = []
for i in range(0,n):
    list_s.append(1/(3*i+1))
T_sum = "{:.2f}".format(sum(list_s))

def series_sum(n):
    list_s = []
    for i in range(0,n):
        list_s.append(1/(3*i+1))
    return "{:.2f}".format(sum(list_s))

# Codewar
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))