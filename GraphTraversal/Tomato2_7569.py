import sys
from collections import deque
M, N, H = list(map(int, sys.stdin.readline().rstrip().split()))
graph = []
moves = [[1, 0, 0],[-1, 0, 0],[0, 1, 0],[0, -1, 0],[0, 0, 1],[0, 0, -1]]
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    graph.append(temp)

queue = deque()
count = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([i, j, k, 0])

def bfs():
    global count
    while queue:
        x, y, z, r = queue.popleft()
        count = max(count, r)

        for move in moves:
            dx, dy, dz = x + move[0], y + move[1], z + move[2]

            if 0 <= dx < H and 0 <= dy < N and 0 <= dz < M and graph[dx][dy][dz] == 0:
                queue.append([dx, dy, dz, r + 1])
                graph[dx][dy][dz] = 1

bfs()

check = False
for k in range(H):
    if any(0 in l for l in graph[k]):
        check = True
        break

if check:
    print(-1)
else:
    print(count)