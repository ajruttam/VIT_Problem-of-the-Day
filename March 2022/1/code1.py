n = int(input())
l = [int(input()) for _ in range(n)]
t = int(input())
f = [0]*n
m = 0
while sum(l):
    for i in range(n):
        l[i] -= t
        m+=t
        if l[i]<0:
            m+=l[i]
            l[i] = 0
        if l[i] == 0 and not f[i]: f[i] = m
        if sum(l)==0: break
print(*f,sep = '\n')