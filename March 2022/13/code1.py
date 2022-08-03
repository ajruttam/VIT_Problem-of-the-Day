l,h,m = input(),int(input()),int(input())
if m == 0:
    print("On",chr(ord(l) + 2*(22 + h%12 + 1)%24))
    print("On",chr(ord(l) + 2*(22 + m//5 +1)%24))
else:
    print("Between",chr(ord(l) + 2*(22 + h%12 + 1)%24),"and",chr(ord(l) + 2*(h%12)))
    if m%5 == 0: print("On",chr(ord(l) + 2*(22 + m//5 +1)%24))
    else: print("Between",chr(ord(l) + 2*(22 + m//5+1)%24),"and",chr(ord(l) + 2*(m//5)))