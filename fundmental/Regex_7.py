# Implement String#to_cents, which should parse prices expressed as $1.23 and return number of cents, or in case of bad format return nil.
import re
def to_cents(amount):
    if bool(re.fullmatch('^\$[0-9]*\.[0-9][0-9]',amount)) == True:
        print(re.sub('(^\$|\.)',"",amount))
    else:
        print("None")

amount = "$9.69$4.3.7"
to_cents(amount)

# import re
# def to_cents(amount):
#     if bool(re.fullmatch('^\$[0-9]*\.[0-9][0-9]',amount)) == True:
#         return int(re.sub('(^\$|\.)',"",amount))

