t, n = input(),input()
nl = len(n)
for i in range(len(t) - nl + 1):
    if sorted(t[i:i+ nl]) == sorted(n):
        print(i+1)