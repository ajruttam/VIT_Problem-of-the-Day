"""
FOR MULTIPLE NUMBERS
TestCase: 10[abc]
Output: abcabcabcabcabcabcabcabcabcabc
"""

# works for more than single digit also
# using index as number

for _ in range(int(input())):
    x = input()
    l = []
    i = 0
    while (i < len(x)):
        if x[i].isdigit():
            n,i = int(x[i]),i+1
            while x[i].isdigit():
                n = 10*n + int(x[i])
                i+=1
            l.append(n)
        elif x[i] == ']':
            a = ""
            while (l[-1] != '['):
                a = l.pop() + a;
            l.pop()
            l.append(l.pop() * a)
            i+=1
        else: 
            l.append(x[i])
            i+=1
    for i in l: print(i, end="")
    print()
