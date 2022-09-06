import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

queue = deque()
queue.append([N, 0])
visited = [False] * 100001
result = [float('inf'), 0]

while queue:
    node, cnt = queue.popleft()

    visited[node] = True

    if cnt > result[0]:
        break

    if node == K:
        result[0] = cnt
        result[1] += 1
        continue
    
    if 0 <= node - 1 < 100001 and not visited[node - 1]:
        queue.append([node - 1, cnt + 1])
        
    if 0 <= node * 2 < 100001 and not visited[node * 2]:
        queue.append([node * 2, cnt + 1])

    if 0 <= node + 1 < 100001 and not visited[node + 1]:
        queue.append([node + 1, cnt + 1])

print(*result, sep="\n")
