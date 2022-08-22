#!/bin/python3
def check(seq, elem):
    if elem in seq:
        T = seq.index(elem)
        print(T)
    else :
        print(False)

seq = [101, 45, 75, 105, 99, 107]
elem = 107
check(seq, elem)
