d2 = {ele:sym for ele, sym in [input().split() for _ in range(int(input()))]}
d1 = {sym:ele for ele,sym in d2.items()}
n,q = eval('d' + input()), input()
print(n[q] if n.get(q) else "Not found")