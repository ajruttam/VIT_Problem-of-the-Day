# Input as string
x = list(map(int,list(input())))
print(abs(sum(x[::2]) - sum(x[1::2])))
