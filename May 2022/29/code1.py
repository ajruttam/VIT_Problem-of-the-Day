n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
s = int(input())
for i in range(n):
    for j in range(n):
        if l[i][j] == -1:continue
        x = 2*abs(i - (l[i][j] - s)//n) + abs(j - (l[i][j] - s)%n)
        print(l[i][j],x,sep = '\t')