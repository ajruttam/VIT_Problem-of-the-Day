x,w1,w2,n = int(input()),int(input()),int(input()),int(input())
l = list(map(int, input().split()))
for i in l:
    print(int((i-x)%w1==0 or (i-x)%w2==0 or (i-x)%(w1+w2)==0),end = ' ')