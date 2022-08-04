v = int(input())%7
n = int(input())
m = int(input())%7
d = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(d[(abs(n - v + 7) + m)%7])