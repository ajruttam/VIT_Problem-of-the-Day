n = int(input())
l = []
for i in range(n):
    r = []
    for j in range(n*2-1):
        if j == n - i - 1 or j == n + i - 1:
            r.append('*')
        else:
            r.append('.')
    l.append(r)
for i in l:
    print(*i,sep = ' ')