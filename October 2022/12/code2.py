#O(n) solution

n = int(input())
for i in range(1,n - 3):
    if (4 * i + 6 == n):
        print(1,i,sep = "\n")
        break
else: print(0)
