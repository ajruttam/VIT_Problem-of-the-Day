n = int(input())
c = input().split()
m = int(input())
l = input()
for i in range(0,len(l) - m):
    if l[i+m] in l[i:i+m]:
        print("Invalid")
        break
else: print("Valid")