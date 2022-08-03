s1 = input()
s2 = input()
s3 = ""
for i in range(1,len(s2)+1):
    c3 = ord(s1[-i]) - ord(s2[-i])
    if c3>0:
        s3+=chr(96+c3)
    elif c3<0:
        s3+=chr(123+c3)
    else:
        s3+=s1[-i]
if len(s1)>len(s2): s3 += s1[:-len(s2)]
print(s3[::-1])