# mplement String#six_bit_number?, which should return true if given object is a number representable by 6 bit unsigned integer (0-63), false otherwise.

# It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.
import re
def six_bit_number(n):
    str_n = str(n)
    print(str_n)
    if re.search(r"^([0-9]{1}|[1-5]?[0-9]?|6?[0-3]?)$",str_n) == None:
        print("false")
    elif n == "":
        print("false")
    else:
        print("true")
n = "5␣5"
six_bit_number(n)


#  CodeWars
# import re
# def six_bit_number(n):
#     return bool(re.fullmatch(r'([1-5]?\d)|(6[0-3])', n))