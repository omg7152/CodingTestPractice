import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().rstrip().split()))
visit = [False for _ in range(100001)]

queue = deque()
queue.append([N, 0])
visit[N] = True
result = 0
while queue:
    num, cnt = queue.popleft()

    if num == K:
        result = cnt
        break

    for i in (num + 1, num - 1, num * 2):
        if 0 <= i <= 100000 and not visit[i]:
            visit[i] = True
            queue.append([i, cnt + 1])
            
print(result)