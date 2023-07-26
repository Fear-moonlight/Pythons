# Write a regex to validate a 24 hours time string. See examples to figure out what you should check for:

# Accepted: 01:00 - 1:00

# Not accepted:

# 24:00
import re
def validate_time(time):
    print(bool(re.fullmatch('(([0]*|[0-1])[0-9]|2[0-3]):[0-5][0-9]',time))) 


time = "23:23"
validate_time(time)