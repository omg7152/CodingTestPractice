from collections import deque
import sys

M, N = list(map(int, sys.stdin.readline().rstrip().split()))

box = []
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().rstrip().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j, 0])

totaldate = 0
while queue:
    x, y, z = queue.popleft()
    box[x][y] = 1
    if totaldate < z:
        totaldate = z
    
    for d in moves:
        dx = x + d[0]
        dy = y + d[1]

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue

        if box[dx][dy] == 0:
            queue.append([dx, dy, z + 1])
            box[dx][dy] = 1

if any(0 in l for l in box):
        print(-1)
else:
    print(totaldate)