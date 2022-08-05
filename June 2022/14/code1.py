l = []
for _ in range(int(input())):
    x = input().split()
    l.append((int(x[0]), x[1]))
print(*sorted(l)[int(input()) - 1])