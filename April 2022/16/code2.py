arr = [int(input()) for i in range(int(input()))]
x = int(input())
m = max(arr)
final = []
for i in arr:
    c = bin(i^x).count('1')
    if c < m: final = [i]; m = c
    elif c == m: final.append(str(i))
print(*final, sep = "\n")