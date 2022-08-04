l = [bin(int(input()))[2:] for _ in range(int(input()))]
m = bin(int(input()))[2:]
mi,f = int(max(l)),[]
for i in l:
    ml = len(i) if len(i) > len(m) else len(m)
    i = (ml - len(i))*'0' + i
    n = (ml - len(m))*'0' + m
    c = sum([1 for j in range(ml) if i[j] != n[j]])
    if mi > c: mi = c; f = [int(i,2)]
    elif mi == c: f.append(int(i,2))
print(*f,sep='\n')