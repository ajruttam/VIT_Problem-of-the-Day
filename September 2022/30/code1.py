n = int(input())
s = 0
for i in range(2,n):
    f = 1
    for j in range(2,i//2+1):
        if i%j == 0:
            f = 0
            break
    if f: s += i
    if n > s: continue
    elif n == s: print("Yes")
    else: print("No")
    break
