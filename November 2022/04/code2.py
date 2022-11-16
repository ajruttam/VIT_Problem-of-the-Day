n = int(input())
l = list(map(int, input().split()))
ne = 0
p = 0
for i in range(n):
    if l[i] < 0: ne += 1
    elif l[i] > 0: p += 1
print((ne*(ne-1))//2 + (p*(p-1))//2)
