n = int(input())
if n%2:
    if ((n//2)%2): print(0)
    else: print(1)
else:
    if ((n//2)%2): print(1)
    else: print(0)