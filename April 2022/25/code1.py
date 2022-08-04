from itertools import combinations
x = int(input())
c = int(input())
l = list(enumerate(map(int, input().split()),1))
for i in combinations(l,4):
    if x == sum([j[1] for j in i]):
        print(*[j[0] for j in i])
        break
else: print("No")