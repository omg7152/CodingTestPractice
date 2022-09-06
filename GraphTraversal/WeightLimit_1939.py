import sys
from collections import deque

def bfs(mid):
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        s = queue.popleft()

        if s == end:
            return True

        for nx, nc in graph[s]:
            if visited[nx] == 0 and mid <= nc:
                queue.append(nx)
                visited[nx] = 1
    return False

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[]for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, sys.stdin.readline().rstrip().split())

low, high = 1, 1000000000

while low <= high:
    visited = [0 for _ in range(n + 1)]
    mid = (low + high) // 2

    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)