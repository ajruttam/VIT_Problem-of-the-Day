def isPrime(n):
    if n == 0 or n == 1: return False
    else: return not sum([1 for i in range(2,int(n**0.5) + 1) if n%i==0],0)

n = int(input())
l = list(map(int,input().split()))
d = {i+1:{"token":l[i], "c":[]} for i in range(n)}
for i in range(n-1):
    x,y = map(int, input().split())
    d[x]['c'].append(y)
for i in range(n,0,-1):
    for j in d[i]['c']:
        d[i]['c'] = list(set(d[j]['c'] + d[i]['c']))
for _ in range(int(input())):
    q = int(input())
    c = 0
    for i in d[q]['c']:
        if isPrime(d[i]['token']): c += 1
    print(c)
