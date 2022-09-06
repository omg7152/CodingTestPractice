import sys
from collections import deque

def down():
    for i in range(6):
        puyoList = []
        for j in range(11, -1, -1):
            if graph[j][i] != ".":
                puyoList.append(graph[j][i])
                graph[j][i] = "."
        
        cnt = 0
        for j in range(11, 11 - len(puyoList), -1):
            graph[j][i] = puyoList[cnt]
            cnt += 1


def pop(x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    poplist = [[x, y]]

    while queue:
        cx, cy = queue.popleft()

        for move in moves:
            dx, dy = cx + move[0], cy + move[1]
            if 0 <= dx < 12 and 0 <= dy < 6 and not visited[dx][dy] and graph[dx][dy] == graph[x][y]:
                visited[dx][dy] = True
                queue.append([dx, dy])
                poplist.append([dx, dy])

    if len(poplist) >= 4:
        for px, py in poplist:
            graph[px][py] = "."
        return True
        
    return False

def search():
    visited = [[False] * 6 for _ in range(12)]
    check = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and not visited[i][j]:
                if pop(i, j, visited):
                    check = True

    if check:
        down()
    return check

moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
graph = []
for _ in range(12):
    graph.append(list(sys.stdin.readline().rstrip()))

ans = 0
while True:
    if not search():
        break
    ans += 1

print(ans)

