s = [int(input()) for _ in range(int(input()))]
d = int(input())
xor = int(input())
for i in s:
    for j in s:
        if abs(i - j) == d and i^j == xor:
            print(*sorted([i,j]),sep = '\t')
            exit()