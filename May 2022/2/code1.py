n = int(input())
w1 = [list(map(int,input().split())) for _ in range(n)]
w2 = [list(map(int,input().split())) for _ in range(int(input()))]
p = 0
for i in range(n): 
    s = sum([w2[j][1] for j in range(len(w2)) if w2[j][0] <= w1[i][0]])
    if s >= w1[i][1]: p+=1
print("Allowed" if p >= (n+1)//2 else "Denied")