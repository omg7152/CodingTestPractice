import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]

for i in range(N - 1):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    queue.append(1)
    visit[1] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visit[i] == False:
                result[i] = v
                visit[i] = True
                queue.append(i)
bfs()
for i in result[2:]:
    print(i)