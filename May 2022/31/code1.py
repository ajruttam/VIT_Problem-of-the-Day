n,m,mw = int(input()),0,{}
w = [input() for _ in range(n)]
c = input()
for i in w:
    s = sum([(j+1)*(c.index(i[j])+1) for j in range(len(i)) if i[j] in c])
    if s >= m:
        m = s
        if s in mw: mw[s].append(i)
        else: mw[s] = [i]
print(*mw[max(mw)],sep = '\n')