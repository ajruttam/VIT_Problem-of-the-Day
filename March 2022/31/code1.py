def power(m,l):
    while(m):
        p = 1
        while(m >= p): p *= 3
        l.append(p//3)
        m -= p//3
        
n = int(input())
l = []

power((n//3)*3,l)

for i in l:
    print(i,end = '\t')

print("\n" + str(sum(l)))