t,z = input().split()
if t == "08:00:00" and z == "A.M":
    print("08:00:00 midmorning")
elif t == "04:00:00" and z == "P.M":
    print("08:00:00 midevening")
elif t == "12:00:00" and z == "midnight":
    print("08:00:00 midnight")
elif t[:2] == "12" and z == "A.M":
    print("08" + t[2:] + " A.M")
elif int(t[:2])//8 == 0 and z == "A.M":
    print(t,z)
elif t[:2] == "08" and z == "A.M":
    print(t + " B.M")
elif int(t[:2])//8 == 1 and z == "A.M":
    print(f"{(int(t[:2]) - 8):02}"+t[2:] + " "+"B.M")
elif t[:2] == "12" and z == "P.M":
    print("04" + t[2:] + " B.M")
elif int(t[:2]) < 4 and z == "P.M":
    print(f"{(int(t[:2]) + 4):02}"+t[2:] + " "+"B.M")
elif t[:2] == "04" and z == "P.M":
    print("08" + t[2:] + " C.M")
else:
    print(f"{(int(t[:2]) - 4):02}"+t[2:] + " "+"C.M")
