from math import sqrt
d = int(input())
x,y = map(float, input().split())
for i in range(1,d):
    s = sqrt(d*d - i*i)
    if s == int(s):
        if abs(s - x) > 1 and abs(i - y) > 1 and x > 1 and y > 1:
            print("Safe")
            break
else: print("Unsafe")