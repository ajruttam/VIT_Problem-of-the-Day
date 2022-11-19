n,l = map(int, input().split())
li = list(map(int, input().split()))
print("YES" if l - (sum(li))/2 > 0 else "NO")
