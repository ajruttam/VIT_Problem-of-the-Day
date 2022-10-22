l = []
for i in range(int(input())):
    l.append(sorted(map(int,input().split())))
l = list(zip(*l))
for i in range(len(l)):
    l[i] = sorted(l[i], reverse = True)
l = list(zip(*l))
for i in l:
    print(*i)
