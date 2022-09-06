import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    change = []

    while queue:
        x, y = queue.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
                if graph[dx][dy] == 0:
                    queue.append([dx, dy])
                else:
                    change.append([dx, dy])
                
                visited[dx][dy] = True

    for cx, cy in change:
        graph[cx][cy] = 0

    return len(change)

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = 0
last = 0
while True:
    cnt = bfs()
    if cnt == 0:
        print(result)
        print(last)
        break

    result += 1
    last = cnt
