a,b,c,n = int(input()),int(input()),int(input()),int(input())
for i in range(1,2*n,2):
    print("{:.2f}".format(-(c + i*a)/b))
