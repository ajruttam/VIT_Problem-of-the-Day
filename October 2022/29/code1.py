a,b,n = map(int, input().split())
x = n/a
if a%b == 0:
    print(-1)
elif n%a == 0 and n%b != 0:
    print(n)
else:
    n += a - n%a
    while True:
        if n%b != 0:
            print(n)
            break
        n += a
