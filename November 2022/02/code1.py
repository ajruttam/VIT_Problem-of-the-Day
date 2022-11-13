n = int(input())
ph = list(map(int, input().split()))
py = list(map(int, input().split()))
gr = list(map(int, input().split()))
l = [ph[i] + py[i] + gr[i] for i in range(n)]
e = l[0]
l.sort(reverse = True)
print("YES" if l.index(e) <= 2 else "NO")
