import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [False] * n

queue = deque()
queue.append([0, graph[0], 0])
visited[0] = True

while queue:
    a, b, c = queue.popleft()

    if a == n - 1:
        print(c)
        break

    for i in range(1, b + 1):
        da = a + i
        if da < n and not visited[da]:
            queue.append([da, graph[da], c + 1])
            visited[da] = True

else:
    print(-1)
