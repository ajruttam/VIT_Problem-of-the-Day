s1,s2 = input(),input()
s1,s2 = sorted([s1[::-1],s2[::-1]],key = len,reverse = True)
carry,nsum = 0, ''
for i in range(len(s1)):
    if i >= len(s2):
        a = ord(s1[i]) + carry
    else:
        a = ord(s1[i]) + ord(s2[i]) + carry
    nsum += str(a%10)
    carry = a//10
nsum = str(carry) + nsum[::-1]
wl = list(map(int,[nsum[:-len(s1)]] + list(nsum[-len(s1):])))
print(*[chr(96 + (i+1)%26) for i in wl],sep = '')