s = input()
g = ''
for i in s:
    if i.isalpha(): g += i
    else:
        l = g
        for j in range(int(i)):
            g += l if j%2 else l[::-1]
print(g)