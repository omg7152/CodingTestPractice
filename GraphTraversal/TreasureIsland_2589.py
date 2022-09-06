import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
graph = []

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            visited = [[False] * m for _ in range(n)]

            queue = deque()
            queue.append([i, j, 0])
            visited[i][j] = True

            while queue:
                x, y, c = queue.popleft()

                if result < c:
                    result = c
                
                for move in moves:
                    dx, dy = x + move[0], y + move[1]

                    if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and graph[dx][dy] == "L":
                        queue.append([dx, dy, c + 1])
                        visited[dx][dy] = True

print(result)