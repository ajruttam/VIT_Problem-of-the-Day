def count(w):
    c = 0
    for i in w:
        if i in "aeiou": c+=1
    return c
w = input()
n = int(input())
s = 0
for i in range(len(w)):
    for j in range(len(w)):
        if count(w[i:j+1]) == n:
            s += 1
print(s)
