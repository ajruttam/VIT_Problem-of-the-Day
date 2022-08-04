from math import pow
l,u,p = int(input()), int(input()), int(input())
ml = pl = powl = u
mu = pu = powu = l
for i in range(l,u+1):
    for j in range(2,p+1):
        if i == sum(list(map(int, list(str(int(pow(i,j))))))):
            if i < ml: ml,pl,powl = i, j, int(pow(i,j))
            if i > mu: mu,pu,powu = i, j, int(pow(i,j))
print(ml,pl,powl)
print(mu,pu,powu)