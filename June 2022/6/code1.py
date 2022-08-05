l = [int(input())]
while (l[-1] != -1):
    l.append(int(input()))
l = l[:-1]
l.insert(int(input())-1,int(input()))
print(*l,"",sep = '\t')
print(*['%.2f'%((l[i] + l[i + 1] + l[i + 2])/3) for i in range(len(l) - 2)],sep = '\t')