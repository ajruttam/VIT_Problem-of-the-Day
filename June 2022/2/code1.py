for _ in range(int(input())):
    x = input()
    l = [i[0] for i in x.split()]
    if l == sorted(l) or l == sorted(l, reverse = True):
        print(x)