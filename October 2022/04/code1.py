def gcd(x,y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x == y:
        return x
    elif x > y:
        return gcd(x-y,y)
    else:
        return gcd(x,y-x)
    
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    x = gcd(x,y)
    z = gcd(x,z)
    print(z)
