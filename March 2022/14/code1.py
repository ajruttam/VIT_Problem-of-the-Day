n = list(input())
s = sorted(n)
print(*[i+1 for i in range(len(n)) if n[i] == s[i]],sep = '\n')