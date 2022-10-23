alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    x,y = input().split()
    a = ""
    for i in y:
        if i not in a:
            a += i
    for i in alph:
        if i not in a:
            a += i
    for i in x:
        print(a[alph.index(i)],end="")
    print()
    
