n, v = input(), int(input())
c = [[n[0],n[1:3],n[3:]],[n[:2],n[2:4],n[-1]],[n[:2],n[2],n[3:]]]
e = ['++','--','-+','+-']
for i in c:
    for j in e:
        x = i[0]+j[0]+i[1]+j[1]+i[2]
        if eval(x) == v:
            print(x)
            exit()