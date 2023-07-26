# Remove HTML tags and return string without:

#     <tag> and </tag>
#     <tag/>
#     <tag />
#     html tags with attributes.
#     Don't trim space, tab etc.

# You have to use regexp.
import re
string = "pippi<a href='https://uk.linkedin.com/in/giacomosorbi'>" 
reg = r'<([A-Za-z !@#$%^&*,.?=0-9:''{}]*)>|</[A-Za-z !@#$%^&*(),.?=0-9:''{}]*>|<[A-Za-z !@#$%^&*(),.?=0-9:''{}]*/>'
T = re.sub(r"<([A-Za-z !@#$%^&*,/.?=0-9:''{}]*)>|</[A-Za-z !@#$%^&*(),.?=0-9:''{}]*>|<[A-Za-z !@#$%^&*(),.?=0-9:''{}]*/>","",string)
print(T)

reg1 = "<[^>]*> --> matches anything but the one in bracket "