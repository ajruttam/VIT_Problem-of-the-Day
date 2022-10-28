n=int(input())
x=list(map(int,input().split()))
l=[]
for i in x:
    c=0
    for j in x:
        if j>i:
            c+=1
    l.append(c)
print(*l)
