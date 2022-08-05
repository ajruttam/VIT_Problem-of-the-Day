d = {i[1]: [i[0]] + i[2:] for i in [input().split() for _ in range(32)]}
int(input()); print(*d[input()])