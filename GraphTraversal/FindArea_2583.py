import sys;
from collections import deque;

M, N, K = list(map(int, sys.stdin.readline().rstrip().split()));
graph = [[0 for _ in range(M)] for _ in range(N)];
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]];
Rectangle = [];

for i in range(K):
    Rectangle.append(list(map(int, sys.stdin.readline().rstrip().split())));

#직사각형 안에 포함된 좌표값 1로 수정
for i in range(N):
    for j in range(M):
        for rec in Rectangle:
            if  rec[0] <= i < rec[2] and rec[1] <= j < rec[3] :
                graph[i][j] = 1;

result= [];

def bfs(i, j):
    #영역의 크기
    count = 0;
    queue = deque();
    queue.append([i, j]);

    while queue:
        x, y = queue.popleft();
        graph[x][y] = 1;
        count += 1;
        for move in moves:
            dx, dy = x + move[0], y + move[1];

            #이동 가능한 칸 중에 방문하지 않은 칸
            if 0 <= dx < N and 0 <= dy < M and graph[dx][dy] == 0:
                graph[dx][dy] = 1;
                queue.append([dx, dy]);
    return count;

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            result.append(bfs(i, j));

result.sort();
print(len(result));
for i in result:
    print(i, end=" ");