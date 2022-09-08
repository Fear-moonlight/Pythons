# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string

x = "45385593107843568"
T_x = [int(a) for a in str(x)]

T_S = []
for i in T_x:
    if i >= 5:
        T_S.append("1")
    else:
        T_S.append("0")
new_str = ''.join(T_S)
print (new_str)
    
def fake_bin(x):
 return ''.join('0' if int(c) < 5 else '1' for c in x)