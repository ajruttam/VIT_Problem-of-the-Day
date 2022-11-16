x,y,n,r = map(int,input().split())
if n*x > r: print(-1)
else:
    pr = min((r - n*x)//(y-x), n)
    print(n - pr, pr)
