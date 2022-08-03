m = int(input())
n = int(input())
matrix = ["".join(sorted(input().split())) for _ in range(m)]
print('Shuffled Row Matrix') if len(set(matrix)) == 1 else print("Not Shuffled Row Matrix")