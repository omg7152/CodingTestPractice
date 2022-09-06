import sys
import heapq

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

sensor = list(map(int, sys.stdin.readline().rstrip().split()))
sensor.sort()

result = []

for i in range(N - 1):
    if sensor[i + 1] - sensor[i] != 0:
        heapq.heappush(result, (sensor[i + 1] - sensor[i]) * -1)

i = 0
while(len(result) != 0 and i != K - 1):
    heapq.heappop(result)
    i += 1

if not result:
    print(0)
else:
    print(sum(result) * -1)
