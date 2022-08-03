s = input()
dl = list(set(list(s)))
l = []
com = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for i in com:
    b = ''
    for j in s:
        if not (dl[i[0]] == j or dl[i[1]] == j):
            b += j
    c = 0
    for a in range(1,len(b)-1):
        if (b[a] == b[a+1] or b[a-1] == b[a]) and c<2:
            continue
        elif c>1:
            break
        else:
            c+=1
    if c<2: l.append(b)
sl = [i for i in l if len(i) == len(max(l,key=len))]
print(min(sl))