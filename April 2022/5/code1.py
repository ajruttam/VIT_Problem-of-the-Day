l = list(map(int,input().split()))
e = ((l[5] - l[0]) + l[7])//2
b = l[7] - e
a = l[0] - b
d = l[9] - e
c = l[6] - d
print(a,b,c,d,e)