# Implement the function which should return true if given object is a vowel (meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.

import re
regex = '^[aeiouAEIOU]*'
def is_vowel(s): 
    print(bool(re.fullmatch('^[aeiouAEIOU]',s)))

s = "Lol"
is_vowel(s)
