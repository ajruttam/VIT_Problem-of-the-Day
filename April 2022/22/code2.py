ud = {6:9,9:6,0:0,8:8,1:1}
diff = int(input())
for i in ud:
    for j in ud:
        if 10*i + j - 10*ud[j] - ud[i] == diff:
            print(f"{ud[j]}{ud[i]} {i}{j}")