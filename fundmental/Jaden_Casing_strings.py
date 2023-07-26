string = "How can mirrors be real if our eyes aren't real"
T = string.split(" ")
list_a =[]
for i in T:
    list_a.append(i[0].upper() + i[1:].lower())
print(" ".join(list_a))

