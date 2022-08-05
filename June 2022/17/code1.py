n1, n2, d = int(input()), int(input()), {}
for _ in range(n1):
    s = input().split()
    d[s[0]] = s[1:]
for i in range(int(input())):
    x,y = input().split()
    d[x], d[y] = d[y], d[x]
for i in d:
    print(i, *d[i], "")