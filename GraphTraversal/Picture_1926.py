import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    cnt = 1
    while queue:
        cx, cy = queue.popleft()

        for move in moves:
            dx, dy = cx + move[0], cy + move[1]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 1 and not visited[dx][dy]:
                visited[dx][dy] = True
                cnt += 1
                queue.append([dx, dy])

    return cnt

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ans = 0
maxSize = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            ans += 1
            maxSize = max(maxSize, bfs(i, j))
            
print(ans)
print(maxSize)
