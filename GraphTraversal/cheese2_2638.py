from collections import deque
import sys

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    change = []

    while queue:
        x, y = queue.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < N and 0 <= dy < M:
                if graph[dx][dy] == 0 and visited[dx][dy] == 0:
                    queue.append([dx, dy])
                    visited[dx][dy] = 1
                elif graph[dx][dy] == 1:
                    if visited[dx][dy] == 2:
                        change.append([dx, dy])
                        visited[dx][dy] = 3
                    elif visited[dx][dy] == 0:
                        visited[dx][dy] = 2

    for cx, cy in change:
        graph[cx][cy] = 0

    return len(change)
        

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

ans = 0

while True:
    cnt = bfs()

    if cnt == 0:
        print(ans)
        break

    ans += 1
