hx,hy,mx,my = int(input()),int(input()),int(input()),int(input())
nh = (hx - 1)*4 + hy//5
nm = (mx - 1)*20 + my
if nh == 0: nh = 12
print(f"{nh:02d}\n{nm:02d}")