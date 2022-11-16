for _ in range(int(input())):
    x = input()
    l = x.split('.')
    ans = "Cannot Be Used as a Proxy"
    if len(l) == 4:
        for i in l:
            if not (i.isdigit() and 0 <= int(i) <= 255):
                break
        else:
            ans = "Can Be Used as a Proxy"
    print(ans)    
