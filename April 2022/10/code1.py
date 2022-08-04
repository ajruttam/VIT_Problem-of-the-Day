a,b,c = sorted([int(input()),int(input()),int(input())])
print(a - b - c if b == 1 else a - b * c)