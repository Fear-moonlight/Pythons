import re
def six_bit_number(n):
    print(bool(re.fullmatch(r"(-?([1-9]|[1-9]\d|1[01]\d|12[0-7]))", n)))

n = "-99"
six_bit_number(n)