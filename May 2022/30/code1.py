n, k = int(input()),int(input())
if n%k: print("Cannot be built")
else:
    if k%2:
        print(*[i for i in range(n//k - 2*(k//2),n//k + 2*(k//2) + 1,2)],sep = '\t')
    else:
        print(*[i for i in range(n//k - 2*(k//2) + 1,n//k + 2*(k//2),2)],sep = '\t')