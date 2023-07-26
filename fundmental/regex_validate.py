import re 
def validate_pin(pin):
    str_pin = str(pin)   
    print(str_pin)
    if re.search(r"^([0-9]{4}|[0-9]{6})$",str_pin) == None:
        print("False")
    else:
        print("True")

pin = "1234\n"
validate_pin(pin)

# T = re.search(r"^[0-9]{4}$",pin)
# print(T)

