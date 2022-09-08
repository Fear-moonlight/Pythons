TXT = "Hello World"[::-1]
S_TXT = TXT.split(" ")
S_TXT.reverse()
T_TXT = " ".join(S_TXT)
print(T_TXT)

def reverse_words(text):
    return ' '.join(w[::-1] for w in str.split(' '))