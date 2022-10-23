from math import ceil
w,n = input(),int(input())
w = w*ceil(2 * n/len(w))
l, ans = {}, -1
for i in range(1,2*n + 1):
    if i <= n: l[i] = w[i-1]
    else:
        l[(2 * n) - i + 1] += (w[i-1])
        if len(set(l[2 * n - i + 1])) == 1:
            ans = 2 * n - i + 1
            break
print(ans)
