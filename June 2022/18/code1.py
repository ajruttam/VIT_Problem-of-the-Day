d,l = {},[]
for i in range(int(input())):
    x = input().split()
    d[x[1]] = x[0]
x = input()
d = dict(reversed(list(d.items())))
for i in d:
    if i == x:
        l.append(d[x])
        x = d[i]
print(*l)