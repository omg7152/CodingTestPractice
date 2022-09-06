import sys;
from collections import deque;

N, M = list(map(int, sys.stdin.readline().rstrip().split()));
graph = [];
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]];

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())));

def bfs():
    queue = deque();
    queue.append([0, 0]);
    while queue:
        x, y = queue.popleft();
        for move in moves:
            dx, dy = x + move[0], y + move[1];
            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue;
            if graph[dx][dy] == 0:
                continue;
            
            if graph[dx][dy] == 1:
                graph[dx][dy] = graph[x][y] + 1;
                queue.append([dx, dy]);
    
    return graph[N - 1][M - 1];

print(bfs());