import sys
import heapq

cnt = int(sys.stdin.readline().strip())
lect = []
for i in range(cnt):
    lect.append(list(map(int, sys.stdin.readline().strip().split())))

lect.sort()

result = []
heapq.heappush(result, lect[0][1])
for i in range(1, len(lect)):
    if lect[i][0] >= result[0]:
        heapq.heappop(result)     
    heapq.heappush(result, lect[i][1])
print(len(result))
