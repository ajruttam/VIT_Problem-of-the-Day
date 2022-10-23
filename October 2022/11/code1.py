def pro(n):
    s = 0
    for i in range(2,n):
        if n%i == 0: s += i
    return s
    
m,n = int(input()), int(input())
if pro(m) > pro(n): print(m)
elif pro(m) < pro(n): print(n)
else: print("No dominance")
