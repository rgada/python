import itertools
import operator

list_1 = [1,2,3,-6,-7,8,10,15,-20]
comb = list(itertools.combinations(list_1,4))
l = len(comb)
print(f"Total sublist: {l}")
sumZero = []

def fun_add(a, b, c, d):
    return a + b + c + d
sumOfAll = list(itertools.starmap(fun_add, comb))
z = list(zip(comb,sumOfAll))
#print(z)
sumZero = list(filter(lambda x: x[1] == 0, z))
print(sumZero)

for sl in comb:
    s = itertools.starmap(fun_add, sl)
    print(s)
    break
    if s == 0:
        sumZero.append(sl)
    """
    sum = 0
    for ele in (sl):
        sum += ele
    if sum == 0:
        sumZero.append(sl)
    """

print(sumZero)