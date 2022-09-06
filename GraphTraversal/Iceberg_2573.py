import sys
from collections import deque

def bfs(i, j):

    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    seaList = []
    
    while queue:
        x, y = queue.popleft()
        seaCount = 0

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < N and 0 <= dy < M:
                if graph[dx][dy] == 0:
                    seaCount += 1
                elif graph[dx][dy] != 0 and not visited[dx][dy]:
                    queue.append([dx, dy])
                    visited[dx][dy] = True

        if seaCount > 0:
            seaList.append([x, y, seaCount])
    
    for cx, cy, cnt in seaList:
        graph[cx][cy] = max(0, graph[cx][cy] - cnt)

    return 1

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
year = 0
ice = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            ice.append((i, j))

while ice:
    visited = [[False] * M for _ in range(N)]
    delList = []
    groupCount = 0

    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            groupCount += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))

    if groupCount > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if groupCount < 2:
    print(0)