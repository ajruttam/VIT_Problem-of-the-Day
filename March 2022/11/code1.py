x = input()
c = 0
for i in range(len(x)):
    x = x[-1] + x[:-1]
    if int(eval('0b' + x))%2 == 0: c+=1
print(c)