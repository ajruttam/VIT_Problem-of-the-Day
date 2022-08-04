n = bin(int(input()))[2:]
ob = n[::2].count('1') if len(n)%2 else n[1::2].count('1')
eb = n[1::2].count('1') if len(n)%2 else n[::2].count('1')
o = n[::2] if len(n)%2 else n[1::2]
e = n[1::2] if len(n)%2 else n[::2]
if ob < eb: print(int('0'.join(e) + '0',2))
else: print(int('0'.join(o),2))