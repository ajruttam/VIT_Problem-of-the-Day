l = int(input())
u = int(input())
for a in range(l,u+1):
    for b in range(l,u+1):
        for c in range(l,u+1):
            if a<=b<=c:
                if (c**2 - a**2 - b**2) == 0:
                    print(a,b,c,"Exactly Pythagorean")
                elif -1 <= (c**2 - a**2 - b**2) <= 1 :
                    print(a,b,c,"Very Close to Pythagorean")
                elif -2 <= (c**2 - a**2 - b**2) <= 2:
                    print(a,b,c,"Close to Pythagorean")