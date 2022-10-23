from itertools import permutations
x = tuple(input())
l = sorted(permutations(x))
print(l.index(x) + 1)
