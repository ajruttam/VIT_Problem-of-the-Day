"""
FOR MULTIPLE NUMBERS
TestCase: 10[abc]
Output: abcabcabcabcabcabcabcabcabcabc
"""

# works for more than single digit also
# using character directly (for-each loop)

for _ in range(int(input())):
    x = input()
    l = []
    f = 0
    for i in x:
        if i.isdigit():
            if f:
                l[-1] = 10*l[-1] + int(i)
            else:
                l.append(int(i))
                f = 1
        elif i == ']':
            a = ""
            while (l[-1] != '['):
                a = l.pop() + a;
            l.pop()
            l.append(int(l.pop()) * a)
        else: 
            l.append(i)
            f = 0
    for i in l: print(i, end="")
    print()
