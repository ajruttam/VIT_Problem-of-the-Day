m,n = sorted([int(input()),int(input())])
q,d = [],[]
while m>0:
    if m%2:
        q.append(m)
        d.append(n)
    m //= 2
    n *= 2
for i in range(len(q)-1,-1,-1):
    print(f"{q[i]} {d[i]}")
print(q[0]*d[0])