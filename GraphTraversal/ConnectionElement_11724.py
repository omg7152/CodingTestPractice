import sys;
from collections import deque;

N, M = list(map(int, sys.stdin.readline().rstrip().split()));

graph = [[] for _ in range(N + 1)];
visited = [False for _ in range(N + 1)];
for i in range(M):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()));
    graph[a].append(b);
    graph[b].append(a);

def bfs(i):
    queue = deque([i]);
    while queue:
        v = queue.popleft();
        for j in graph[v]:
            if not visited[j]:
                queue.append(j);
                visited[j] = True;

result = 0;
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i);
        result += 1;

print(result);
