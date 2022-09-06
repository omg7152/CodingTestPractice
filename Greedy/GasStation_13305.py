import sys

N = int(sys.stdin.readline().rstrip())

distance = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
pay = price[0]
for i in range(N - 1):
    pay = min(pay, price[i])
    result += distance[i] * pay

print(result)
