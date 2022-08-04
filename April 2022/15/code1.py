for _ in range(int(input())):
    x,y,z = map(int,input().split())
    print(y * (1 + int((z - x)*3//(2*x))))