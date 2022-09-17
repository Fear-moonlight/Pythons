# Write function which takes a string and make an acronym of it.

# Rule of making acronym in this kata:

#     split string to words by space char
#     take every first letter from word in given string
#     uppercase it
#     join them toghether

# Eg:

# Code wars -> C, w -> C W -> CW

# Note: There will be at least two words in the given string!

string = "code war"
T = string.split(" ")
print("".join(i[0].upper() for i in T))

# code War

def to_acronym(input):
  # only call upper() once
  return ''.join(word[0] for word in input.split()).upper()

