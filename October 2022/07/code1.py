n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
for i in range(n):
    if l1[i] > l2[i]:
        l1[i],l2[i] = l2[i], l1[i]
print(*l1)
print(*l2)
