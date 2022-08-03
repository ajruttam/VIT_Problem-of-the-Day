n = int(input())
k = int(input())
l = ''
while n>0:
    l += str(n%k)
    n //= k
print(l[::-1],sum([int(i) for i in l]),sep = '\n')