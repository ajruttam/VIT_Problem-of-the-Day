def string(n,s):
    l = ['r','g','b']
    while n != 0:
        r = n%3
        s += l[r]
        n //= 3
    s = (s + 'r'*(20-len(s)))
    return s
def compare(s,t,a):
    while True:
        t += 1
        order = t
        c = 0
        s1 = string(t,'')
        c = sum([1 for i in range(20) if s[i] != s1[i]])
        if c != a: continue
        else: break
    return [order,s1]
n = t = x = int(input())
s = string(n,'')
second,s1,third,s2 = compare(s,t,1)+compare(s,t,2)
print(second,third,sep = '\t')
print(s[::-1],s1[::-1],s2[::-1],sep = '\n')