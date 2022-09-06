#Q2
import sys;
from collections import deque;
N, M = list(map(int, sys.stdin.readline().rstrip().split()));

graph = [];
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())));

moves = [[0, 1], [1, 0], [0, -1], [-1, 0]];

def bfs(x, y):
    queue = deque();
    queue.append((x, y));
    while queue:
        x, y = queue.popleft();

        for move in moves:
            dx = x + move[0];
            dy = y + move[1];

            if dx < 0 or  dx >= N or dy < 0 or dy >= M:
                continue;

            if graph[dx][dy] == 0:
                continue;

            if graph[dx][dy] == 1:
                graph[dx][dy] = graph[x][y] + 1;
                queue.append((dx, dy));

    return graph[N - 1][M - 1];

print(bfs(0,0));