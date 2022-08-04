n = input()
m = int(input())
l = list(map(int,list(n[-m:])))
n = int(n[-m:])
while n >= sum(l[-m:]):
    if n == sum(l[-m:]):
        print("Generated")
        break
    l.append(sum(l[-m:]))
else: print("Cannot be generated")