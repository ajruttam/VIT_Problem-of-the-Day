s1, s2 = input(), input()
s3 = ''
for i in range(len(s1)):
    x = abs(ord(s1[i]) - ord(s2[i])) + ord(s2[i])
    x = x if x < 91 else x - 26
    s3 += chr(x)
print(s3)