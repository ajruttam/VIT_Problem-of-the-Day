n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
xs = xb = ys = yb = p = d = 0
for i in range(n):
    for j in range(n):
        if l[i][0] == l[j][0]:
            if d < abs(l[i][1] - l[j][1]):
                d = abs(l[i][1] - l[j][1])
                xs,xb,ys,yb = l[i][0],l[i][0],*sorted([l[i][1],l[j][1]])
                p = [l[k][0] for k in range(n)].count(xs)
print(xs,ys)
print(xb,yb)
print(d,p,sep = '\n')