import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()
for i in range(m):
    x = heapq.heappop(num)
    y = heapq.heappop(num)

    heapq.heappush(num, x + y)
    heapq.heappush(num, x + y)

print(sum(num))
    