d = []
for _ in range(int(input())):
    d += list(input())
print(max(d, key = d.count))