def sumfib(n):
    a, b, som = 0, 1, 2
    for i in range(1, n-2):
        a, b = b, a+b
        som += b
    return som
n,m = int(input()),sumfib(int(input()))
if (m*n)%3: print(n//3*3, m*(n//3*3))
else: print(n,m*n)