= int(input())
s = sum(list(map(int,input().split())))
print("No" if s/n%1 else f"Yes\n{s//n}")