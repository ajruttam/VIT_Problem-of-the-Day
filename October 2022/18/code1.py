n = input()
l = len(n)
for i in range(l-1,0,-1):
    if (int(n[:l-i])%i != 0):
        print("No")
        break
else:
    print("Yes")
