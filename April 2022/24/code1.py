bl = []
ml = []
m = 51
for _ in range(int(input())):
    a,b,k = map(float,input().split())
    i = a
    l = [int(a)]
    while (i+k < b + 0.001):
        i += k
        l.append(round(i,1) if round(i,1) != int(round(i,1)))
    bl.append(l)
    if len(l) < m: ml,m = l,len(l)
s = [i for i in ml for j in bl if i in j]
print(*[i for i in sorted(set(s)) if s.count(i) == len(bl)])