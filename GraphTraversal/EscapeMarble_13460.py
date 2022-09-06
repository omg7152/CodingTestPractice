import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

red = []
blue = []
hole = []
graph = []
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(n):
    line = list(sys.stdin.readline().rstrip())
    graph.append(line)

    for j in range(len(line)):
        if line[j] == 'R':
            red = [i, j]
        if line[j] == 'B':
            blue = [i, j]
        if line[j] == 'O':
            hole = [i, j]

def move(x, y, dx, dy):
    cnt = 0

    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
            x, y = x + dx, y + dy
            cnt += 1

    return x, y, cnt

def solution():
    queue = deque()
    queue.append([red[0], red[1], blue[0], blue[1], 1])
    visit[red[0]][red[1]][blue[0]][blue[1]] = True
    while queue:
        rx, ry, bx, by, count = queue.popleft()

        if count > 10:
            break

        for dx, dy in moves:
            nrx, nry, rcnt = move(rx, ry, dx, dy)
            nbx, nby, bcnt = move(bx, by, dx, dy)

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(count)
                    return

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy

                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    queue.append([nrx, nry, nbx, nby, count + 1])

    print(-1)

solution()