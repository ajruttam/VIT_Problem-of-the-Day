x = input()
m = f = 0
for i in range(len(x)):
    l = int(x)
    for i in range(2,l):
        if l%i == 0:
            if l//i > m:
                m = l//i
                f = l
            break
    x = x[1:] + x[0]
print(m,f,sep="\n")
