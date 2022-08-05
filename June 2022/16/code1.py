d = {}
for i in range(int(input())):
    x = list(map(int, input().split()))
    d[x[0]] = x[2:]
source, dest = int(input()), int(input())
if dest in d[source]: print("Yes")
else:
    for i in d[source]:
        if dest in d[i]: print("Yes"); break
    else: print("No")