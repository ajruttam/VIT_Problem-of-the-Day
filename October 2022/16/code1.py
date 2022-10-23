f,h,d,n = int(input()),int(input()),int(input()),int(input())
p,s = {},0
for i in range(n):
    x = int(input())
    if x in p: p[x].append(int(input()))
    else: p[x] = [int(input())]
while(len(p[d]) != 1):
    p[d].sort()
    l = sum(p[d][:2])
    s += l
    p[d] = p[d][2:]
    p[d].append(l)
print(s)
