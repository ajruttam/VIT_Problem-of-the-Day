n = int(input())
l = list(map(int,input().split()))
s = set([(i,j) for i in l for j in l])
print(len(s))
print(*[l[i] for i in range(n) if l[i] not in l[:i]])