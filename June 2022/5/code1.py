s1,s2 = input().split(), input().split()
for i in range(len(s1)):
    if s1[i] > s2[-i-1]: continue
    else: print("No"); break
else: print("Yes")