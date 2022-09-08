def xo(s):
    T = s.lower()
    if T.count("x") == T.count("o"):
        print(True)
    else:
        print(False)
s = "Xxo"
xo(s)