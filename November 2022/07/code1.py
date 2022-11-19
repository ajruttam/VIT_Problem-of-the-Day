def fact(n):
    i = 1
    if n == 1: return (1,1)
    while True:
        if n%i == 0: n /= i
        else: break
        i += 1
    return (i-1, n==1)

def SF(n):
    c = 1
    for i in range(n,0,-2):
        c *= i
    print(c)
    
n = int(input())
a, f = fact(n)
if f:
    if (a%2): SF(a)
    else: SF(a)
else: print(-1)
