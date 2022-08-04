n = int(input())
s = ''.join([input() for _ in range(n)])*2
m = ''.join([input() for _ in range(n)])
print("Not Shuffled" if m in s else "Shuffled")