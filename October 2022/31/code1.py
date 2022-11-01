a,b = map(int, input().split())
ar = int(a**0.5)
c1 = int(b**0.5)
c2 = c1**2 + c1
br = c1 - 1*(b<c2)
print("Limak" if br<ar else "Bob")
