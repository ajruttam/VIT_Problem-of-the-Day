n = int(input())
l = list(map(int,input().split()))
d = abs(l[1] - l[0])
ind_list = [d-1]
print(l[0],end = ' ')
while d!=0:
    print(l[d-1],end = ' ')
    d = abs(l[d-1]-l[d])
    if d == 0:
        print("\nHappy")
    elif (d-1) in ind_list:
        print("\nAngry")
        break
    ind_list.append(d-1)