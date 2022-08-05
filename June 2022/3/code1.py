n, h, l = input(), int(input()), []
for i in range(len(n)):
    for j in range(i+1, len(n)):
        s = sum(list(map(int, list(n[i:j+1]))))
        if s == h: l.append(n[i:j+1])
print(*l, sep = '\t')