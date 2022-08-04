l = [input().lower() for i in range(int(input()))]
c = lp = 0
for i in l:
    p = 1
    l1,l2 = sorted([i[0],i[-1]])
    p += sum([1 for j in i[1:-1] if l1 > j or l2 < j])
    c += abs(lp - p)
    if lp < p: print('f',abs(lp - p),sep = '\t')
    elif lp == p: print('n',0,sep = '\t')
    else: print('b',abs(lp - p),sep = '\t')
    lp = p
print(c)