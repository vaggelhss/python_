#ASKISI 13 (MaxDistance)

from itertools import combinations

test = [1,3,5,6,77]

def sub_lists(alist, maxnum):
    sublist = [[]]
    for i in range(0, len(alist)+1):
        for subset in combinations(alist, i):
            sublist.append(subset)
    result = 0
    for i in sublist:
        elementsum = 0
        for j in i:
            elementsum += j
        if elementsum > result and elementsum <= maxnum:
            result = elementsum
    return result

print(sub_lists(test, 79))