import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    count = 0

    while queue:
        cx, cy = queue.popleft()
        count += 1

        for move in moves:
            dx, dy = cx + move[0], cy + move[1]

            if 0 < dx <= n and 0 < dy <= m and not visited[dx][dy] and graph[dx][dy] == 1:
                queue.append([dx, dy])
                visited[dx][dy] = True

    return count


n, m, k = map(int, sys.stdin.readline().rstrip().split())
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[False] * (m + 1) for _ in range(n + 1)]
graph = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not visited[i][j] and graph[i][j] == 1:
            ans = max(ans, bfs(i, j))

print(ans)