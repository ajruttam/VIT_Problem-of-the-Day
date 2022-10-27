for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = set(l)
    ls = len(s)
    if ls == n and n%2: print("NO")
    else: print("YES")
