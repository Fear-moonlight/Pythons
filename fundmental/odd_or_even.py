# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr):
    if len[arr] == 0:
        return [0]
    elif sum(arr) % 2 == 0:
        return "even" 
    else :
        return "odd"

#codeWar

def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]
