# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.

# Example:

# ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
# # 


string = "abracadabra"
T = string.count("a")
print(T)

list_a = []

for i in string:
    j = string.count(i)
    tuple_a = (i,j)
    if tuple_a not in list_a:
        list_a.append(tuple_a) 
    # list_a.append(tuple(str(string.count(i))))
print(list_a)

# code War

from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def ordered_count(seq):
    return list(OrderedCounter(seq).items())