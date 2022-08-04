n = int(input())
a = list(map(int,input().split()))
if a[0] != 1: print('No',1,sep = '\n');exit()
for i in range(1,n):
    if i%2 == 0:
        if a[i] != a[i//2] + a[i//2 - 1]:
            print("No",i+1,sep = '\n')
            break
    else:
        if a[i] != a[i//2]:
            print("No",i+1,sep = '\n')
            break
else: print("Yes")
