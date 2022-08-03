m = bin(int(input()))[2:]
n = bin(int(input()))[2:]
m = '0'*(32-len(m)) + m
n = '0'*(32-len(n)) + n
print(*[32 - i for i in range(31,-1,-1) if m[i] == n[i]])