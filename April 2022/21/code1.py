convert = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
s = input()   
out = prev1 = prev2 = prev3 = 0
for i in range(len(s)):
    if prev3 < convert[s[i]] and prev2 < convert[s[i]] and prev1 < convert[s[i]] and i >= 3:
        print("Invalid");exit()
    elif 'LL' in s or 'VV' in s or 'DD' in s: 
        print("Invalid");exit()
    elif prev3 < convert[s[i]] and prev2 != prev3:
        out += convert[s[i]] - 2*prev3
    elif prev2 + prev3 < convert[s[i]]:
        out += convert[s[i]] - 2*(prev2 + prev3)
    else:
        out+= convert[s[i]]
    prev1, prev2, prev3 = prev2, prev3, convert[s[i]]
print(out)