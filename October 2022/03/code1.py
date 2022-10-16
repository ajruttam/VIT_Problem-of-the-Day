# works for single digit numbers only

for _ in range(int(input())):
    x = input()
    l = []
    for i in x:
        if i == ']':
            a = ""
            while (l[-1] != '['):
                a = l.pop() + a;
            l.pop()
            l.append(int(l.pop()) * a)
        else: l.append(i)
    for i in l: print(i, end="")
    print()
            
