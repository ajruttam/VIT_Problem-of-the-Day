x,w1,w2,n = int(input()),int(input()),int(input()),int(input())
l = list(map(int, input().split()))
for i in l:
    print(int(not((i-x)%w1 and (i-x)%w2 and (i-x)%(w1+w2))),end = ' ')