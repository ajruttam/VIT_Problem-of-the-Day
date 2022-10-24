for _ in range(int(input())):
    n = int(input())
    x = input().lower()
    c = 0
    for i in range(n-1):
        if x[i] == x[i+1]:
            c += 1
    print(c)
