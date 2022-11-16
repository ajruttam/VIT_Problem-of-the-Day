n = int(input())
l = list(map(int, input().split()))
c = 0
for i in range(n):
    for j in range(n):
        if i < j:
            if l[i]*l[j] > 0:
                c += 1
print(c)
