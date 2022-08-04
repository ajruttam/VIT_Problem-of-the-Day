w,wd,t,td,l = input(), input(), input(), input(),""
while l != w:
    l,w = w, w.replace(t,td,1)
    if w == wd: print("Yes"); break
else: print("No")