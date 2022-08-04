r,c = int(input()),int(input())
m = [list(map(int,input().split())) for i in range(r)]
zm,l,a = 0,[],[]
for i in range(r-1):
    for j in range(c-1):
        s = m[i][j] + m[i+1][j] + m[i][j+1]+ m[i+1][j+1]
        if s >= zm:
            zm = s
            a.append([i+1,j+1])
            l.append([m[i][j],m[i][j+1],m[i+1][j],m[i+1][j+1]])
print(zm)
for i in l:
    if sum(i) == zm:
        print(*a[l.index(i)],sep='\t')
        print(*i,sep = '\t')