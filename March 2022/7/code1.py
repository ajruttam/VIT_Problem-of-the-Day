n = int(input())
m = int(input())
l = [i for i in range(1,m+1) if m%i == 0]
print("On") if len(l)%2 else print("Off")