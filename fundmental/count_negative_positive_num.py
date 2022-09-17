arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
positive_arr = []
negative_arr = []
for i in arr:
    if i > 0:
        positive_arr.append(i)
    elif i <= 0:
        negative_arr.append(i)
P = len(positive_arr)
N = sum(negative_arr)
print([P,N])

#codeWar
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []