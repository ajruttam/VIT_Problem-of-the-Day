p = int(input())
s = int(input())
n = int(input())
plants = water = p
for i in range(1,n-1,2):
    plants += s
    water += plants
print(plants,water,sep = '\n')