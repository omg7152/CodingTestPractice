import sys;
from collections import deque;
import copy;
N, M = list(map(int, sys.stdin.readline().rstrip().split()));
graph = [];
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]];
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())));

result = 0;
def bfs():
    global result;
    c = copy.deepcopy(graph);
    queue = deque();
    for i in range(N):
        for j in range(M):
            if c[i][j] == 2:
                queue.append([i, j]);
    while queue:
        x, y = queue.popleft();
        for move in moves:
            dx, dy = x + move[0], y + move[1];
            if 0 <= dx < N and 0 <= dy < M:
                if c[dx][dy] == 0:
                    c[dx][dy] = 2;
                    queue.append([dx, dy]);

    cnt = 0;
    for i in c:
        cnt += i.count(0);
    result = max(cnt, result);

def well(x):
    if x == 3:
        bfs();
        return;
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1;
                well(x + 1);
                graph[i][j] = 0;

well(0);
print(result);

