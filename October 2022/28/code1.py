n = int(input())
x = list(map(int, input().split()))
d = {}
for i in x:
    if i in d: d[i] += 1
    else: d[i] = 1
for i in x:
    print(n - x.index(i) - d[i], end = " ")
