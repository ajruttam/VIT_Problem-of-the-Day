x, f = input(), 1
for i in range(len(x)):
    if i == 2 or i == 3 or i == 4:
        if not (x[i] >= "A" and x[i] <= "Z"):
            f = 0
    else:
        if not x[i].isdigit():
            f = 0
if f: print("YES",int("20" + x[:2])+4,sep = "\n")
else: print("NO")
