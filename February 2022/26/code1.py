s = input().split()
d = {}
vowels = ['a','e','i','o','u']
for word in s:
    count = 0;char = ''
    for i in word:
        if i in vowels:
            if char < i:
                count+=1
            elif char == i:
                continue
            else:
                count = 0
                break
            char = i
    if count:
        d.setdefault(count, [])
        d[count].append(word)
print(*d[max(d)],sep = '\n')