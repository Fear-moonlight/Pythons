# Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), false otherwise.
import re
def is_letter(s):
    print(bool(re.fullmatch('^[A-Za-z]',s))) 

s = "7"
is_letter(s)