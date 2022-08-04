def check(i,p):
    c = sum([1 for j in i if j in p])
    if c == len(p):
        print("".join(sorted(i)),"Lucky Player",sep = '\n')
        exit()
    
r,c = int(input()),int(input())
matrix = [input().split() for i in range(r)]
inv = list(zip(*matrix))
p = input()
for i in matrix: check(i,p)
for i in inv: check(i,p)
print("Unlucky Player")