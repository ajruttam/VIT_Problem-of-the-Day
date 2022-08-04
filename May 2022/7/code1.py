l = input().split()[:-1]
n = int(input())
print(*[" ".join(l[i : i + n]) for i in range(len(l) - n, -1, -n)])