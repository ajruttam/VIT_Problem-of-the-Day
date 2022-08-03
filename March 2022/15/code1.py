n = int(input())
l = [input() for _ in range(n)]
w = input()
num = [int(input()) for _ in range(4)]
for i in l:
    if w[num[0]-1] == i[0] and w[num[1]-1] == i[1] and w[num[2]-1] == i[2] and w[num[3]-1] == i[3]:
        print("Valid")
        break
else: print("Invalid")