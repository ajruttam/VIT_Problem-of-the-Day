n = int(input())
if n == 0 or n == 1: print("impossible")
else:
    for i in range(n,0,-1):
        print("*"*i + " "*(2*(n-i+1)-1)+ "*"*i)
    for i in range(2,n+1):
        print("*"*i + " "*(2*(n-i+1)-1) + "*"*i)
