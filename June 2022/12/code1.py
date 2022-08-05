r,c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]
ch,n = int(input()), int(input())
if ch == 1:
    m.insert(n - 1, input().split())
    for i in m: print(*i, "")
elif ch == 2:
    m.remove(m[n-1])
    for i in m: print(*i, "")
elif ch == 3: print(sum(m[n-1]))
else: print(sum([1 for i in m[n-1] if not i%2]))