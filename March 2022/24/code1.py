t = "".join(sorted(set("".join(input().lower().split()))))
c = 1
for i in range(int(input())):
    l = input()
    if "".join(sorted(set("".join(l.lower().split())))) == t:
        print(l)
        c = 0
if (c): print("No such book")