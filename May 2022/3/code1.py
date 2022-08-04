n,so = int(input()),0
s = sorted(list(map(int,input().split())))
for i in range(0,n//2):
    s.insert(2*i+1,s.pop())
    so += s[2*i+1] - s[2*i]
print(*s)
print(so)