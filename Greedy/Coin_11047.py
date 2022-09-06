import sys

N, K = list(map(int, sys.stdin.readline().rstrip().split()))
coins = []

for i in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse=True)

result = 0
for coin in coins:
    result += K // coin
    K = K % coin

print(result)
