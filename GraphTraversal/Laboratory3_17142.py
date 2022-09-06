import sys
from collections import deque
from itertools import combinations

def bfs():
    global ans
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                cnt += 1 

    while queue:
        x, y, c = queue.popleft()

        if ans < c:
            return 

        if graph[x][y] == 0:
            cnt -= 1

        if cnt == 0:
            ans = min(ans, c)
            return

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] != 1 and not visited[dx][dy]:
                queue.append([dx, dy, c + 1])
                visited[dx][dy] = True

N, M = map(int, sys.stdin.readline().rstrip().split())
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

virus = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append([i, j])

ans = float("inf")
for combi in list(combinations(virus, M)):
    visited = [[False] * N for _ in range(N)]
    queue = deque()
    for v in combi:
        x, y = list(v)
        queue.append([x, y, 0])
        visited[x][y] = True

    bfs()

print(ans if ans != float("inf") else -1)