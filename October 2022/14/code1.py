n = int(input())
l = []
for i in range(1,n+1):
    if n%i == 0:
        if n//i >= i:
            l.append((i,n//i))
print(len(l))
for i in l:
    print(*i)
