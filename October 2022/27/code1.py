from math import sqrt
n = sum(list(map(int,list(input()))))
if n%2:
    a=[12321,12345,56789]
    for i in a:
        if str(n) == str(n)[::-1]:
            print(i)
else:
    a=[11111,12345,99856]
    for i in a:
        if sqrt(i)%1 == 0:
            print(i)
