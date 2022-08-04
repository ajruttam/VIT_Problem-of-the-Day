n,k = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]
kl, m = 0, 0
for i in range(n - k + 1):
    s = sum([j[1] for j in l[i:i+k]])
    if s > kl: kl,m = s, l[i][0]
print(m)