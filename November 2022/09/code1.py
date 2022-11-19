m = input()
r = w = ""
for i in m:
    if i.isalpha(): r += i
    elif i.isdigit():
        if w == "" or w[-1] == "(" or w[-1] < i:
            w += i
        elif w[-1] > i:
            while(w[-1] > i):
                r += w[-1]
                w = w[:-1]
                if w == "" or w[-1] == "(": break
            w += i
    elif i == '(': w += i
    else:
        a = 1
        for j in w[::-1]:
            if j == '(': break
            r,a = r+j,a+1
        w = w[:-a]
for i in w[::-1]: r += i
print(r)
