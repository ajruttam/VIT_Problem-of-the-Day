m = int(input())
lm = list(map(int,input().split()))
n = int(input())
lm += list(map(int,input().split()))
m1,m2 = [],[]
for i in sorted(lm):
    if i%5: m2.append(i)
    else: m1.append(i)
for i in m1: print(i,end = ' ')
print()
for i in m2: print(i,end = ' ')