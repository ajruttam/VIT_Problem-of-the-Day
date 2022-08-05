d = {}
for i in range(int(input())):
    for j in range(int(input())):
        x = input().split()
        if x[0] in d: d[x[0]].append(x[1])
        else: d[x[0]] = [x[1]]
print(*d[input()])