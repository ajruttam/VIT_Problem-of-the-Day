x = int(input())
a,flag,f = 0, 1, 0
for _ in range(int(input())):
    l,b,c = map(int, input().split())
    if c <= x:
        flag = 0
        if a < l*b: a = l*b; f = f"{l} {b} {c}"
print("No laptop" if flag else f)