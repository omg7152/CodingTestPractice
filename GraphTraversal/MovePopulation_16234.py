import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().rstrip().split())
graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs(i, j):

    queue = deque([[i, j]])
    temp = [[i, j]]
    visited[i][j] = True
    total = graph[i][j]
    while queue:
        x, y = queue.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and L <= abs(graph[x][y] - graph[dx][dy]) <= R:
                queue.append([dx, dy])
                temp.append([dx, dy])
                visited[dx][dy] = True
                total += graph[dx][dy]

    if len(temp) > 1:
        group.append(temp)
        change.append(total // len(temp))

result = 0
while True:
    group = []
    change = []
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)

    if len(group) > 0:
        result += 1
        for i in range(len(group)):
            for x, y in group[i]:
                graph[x][y] = change[i]

    else:
        break

print(result)