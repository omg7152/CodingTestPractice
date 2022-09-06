import sys
from collections import deque

def bfs(x):
    global maxPC, ans
    queue = deque()
    queue.append(x)
    visited = [False] * (N + 1)
    visited[x] = True
    result = 0
    
    while queue:
        result += 1
        curr = queue.popleft()

        for next in graph[curr]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

    if maxPC < result:
        maxPC = result
        ans = [x]
    elif maxPC == result:
        ans.append(x)


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b].append(a)

maxPC = 0
ans = []
for i in range(1, N + 1):
    bfs(i)

print(*ans, sep=" ")