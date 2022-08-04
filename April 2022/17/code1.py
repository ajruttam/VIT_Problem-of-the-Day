n = int(input())
a = input().split()
f = input().split()
c = 0
for i in range(n):
    if a[i]!= f[i]:
        a[a.index(f[i])],a[i] = a[i],a[a.index(f[i])]
        c += 1
print(c)