# Implement String#eight_bit_number?, which should return true if given object is a number representable by 8 bit unsigned integer (0-255), false otherwise.

# It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.
import re
def six_bit_number(n):
    print(bool(re.fullmatch(r'([0-9]{1}|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])', n)))

for i in range(0,255):
    print(i)
    six_bit_number(str(i))