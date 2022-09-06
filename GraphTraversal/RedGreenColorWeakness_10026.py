import sys
from collections import deque
import copy
N = int(sys.stdin.readline().rstrip())

graph1 = []
moves = [[0, 1],[0, -1],[1, 0],[-1, 0]]
visited1 = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph1.append(list(sys.stdin.readline().rstrip()))

graph2 = copy.deepcopy(graph1)
for i in range(N):
    for j in range(N):
        if graph2[i][j] == "G":
            graph2[i][j] = "R"

def bfs(graph, visited, i, j):
    queue = deque()
    queue.append([i, j])
    color = graph[i][j]
    while queue:
        x, y = queue.popleft()
        graph[x][y] = True
        for move in moves:
            dx, dy = x + move[0], y + move[1]
            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue

            if graph[dx][dy] == color and not visited[dx][dy]:
                queue.append([dx, dy])
                visited[dx][dy] = True

result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if  not visited1[i][j]:
            bfs(graph1, visited1, i, j)
            result1 += 1

        if  not visited2[i][j]:
            bfs(graph2, visited2, i, j)
            result2 += 1

print(str(result1) + " " + str(result2))