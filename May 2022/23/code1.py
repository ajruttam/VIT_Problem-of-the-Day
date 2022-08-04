s = input()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print(s + s[:-(len(s) - i + 1)][::-1])
        break
else: print(s + s[::-1])