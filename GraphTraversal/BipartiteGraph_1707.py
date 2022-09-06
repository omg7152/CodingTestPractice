import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())

result = []

def bfs(i, group):
    queue = deque([i])
    visited[i] = group

    while queue:

        x = queue.popleft()

        for j in graph[x]:
            if not visited[j]:
                queue.append(j)
                visited[j] = -1 * visited[x]
            elif visited[x] == visited[j]:
                return False

    return True

for _ in range(K):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        graph[a].append(b)
        graph[b].append(a)
        
    temp = "YES"
    for i in range(1, V + 1):
        if not visited[i]:
            if not bfs(i, 1):
                temp = "NO"
                break
    result.append(temp)

for msg in result:
    print(msg)
