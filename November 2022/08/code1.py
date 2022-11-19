a,b = list(input().strip()), list(input().strip())
x,i,l = [],0,len(a)
while True:
    if a[i] in b:
        b.remove(a[i])
    else: x.append(a[i])
    i += 1
    if '1' in b and x == []: 
        a = x = ['1']
        l,i = 1,0
    if i == l: break
if b != [] and int("".join(b)) == 0: print("-1.00")
else:
    if b == []: b = ['1']
    print("{:.2f}".format(int("".join(x))/int("".join(b))))
