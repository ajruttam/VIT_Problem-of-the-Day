from math import gcd
for _ in range(int(input())):
    x,y = map(int, input().split())
    if gcd(x,y) != 1: print("IMPOSSIBLE")
    else: print((x - 1)*(y - 1))