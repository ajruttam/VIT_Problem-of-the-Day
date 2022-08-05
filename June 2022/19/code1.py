name, tshirts = [], []
for _ in range(int(input())):
    option = int(input())
    if option == 1:
        name += input().split()[1:]
    elif option == 2:
        tshirts = input().split()[1:][::-1] + tshirts
    else:
        k = int(input())
        for ki in range(k):
            print(name[ki], tshirts[ki])