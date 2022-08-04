n = int(input())
l = list(map(int, input().split()))
for i in range(n-1):
    if i%2 and l[i-1] > l[i]:
        l[i - 1],l[i] = l[i], l[i-1]
    elif i%2 == 0 and l[i+1] < l[i]:
        l[i + 1],l[i] = l[i], l[i+1]
    elif i%2 and l[i+1] > l[i]:
        l[i + 1],l[i] = l[i], l[i+1]
print(*l)