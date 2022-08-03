r = int(input())
c = int(input())
old = [list(map(int,input().split())) for _ in range(r)]
new = []
for i in range(r):
    row = []
    for j in range(c):
        rm = max(old[i])
        cm = min([k[j] for k in old])
        row.append(old[i][j]+rm+cm)
    new.append(row)
for l in new:
    print(*l,end = ' \n')