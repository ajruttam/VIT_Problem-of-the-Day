#O(1) solution

n = int(input())
print(*[1, (n - 6)//4] if (n - 6)%4 == 0 else [0], sep = "\n")
