# using Regular expression
import re
x = input()
if re.match("[0-9]{2}[A-Z]{3}[0-9]{4}", x):
    print("YES",int("20" + x[:2])+4,sep = "\n")
else: print("NO")
