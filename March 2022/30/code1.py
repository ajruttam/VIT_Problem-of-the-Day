n = input()
old = ''
while n:
    for i in range(len(n) - 2):
        if len(set(n[i:i+3])) == 3:
            n = n[: i] + n[i + 3 :]
            break
    if old == n: break
    old = n
if n: print(n)
else: print("No fruit is left over")