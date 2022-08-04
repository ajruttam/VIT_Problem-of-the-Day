r, c, count = int(input()), int(input()), 0
l = [input().split() for i in range(r)]
s = set([l[i][j] for i in range(r) for j in range(c)])
if s == {'l', 'x', 'z'}:
    for i in range(r - 1):
        for j in range(c - 1):
            if (l[i][j] == l[i+1][j] == l[i+1][j+1] == 'l'):
                count += 1
    print(count)         
else: print("Invalid")