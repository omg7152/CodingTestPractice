import sys
from collections import deque

R, C = map(int, sys.stdin.readline().rstrip().split())

graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

S = []
water = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == "S":
            S = [i, j]
            graph[i][j] = "."
        if graph[i][j] == "*":
            water.append((i, j))

def check(x, y):
    for move in moves:
        dx, dy = x + move[0], y + move[1]

        if 0 <= dx < R and 0 <= dy < C and graph[dx][dy] == "*":
            return False
    return True

def changeWater():
    global water
    addWater = []
    for wx, wy in water:
        for move in moves:
            dx, dy = wx + move[0], wy + move[1]
            if 0 <= dx < R and 0 <= dy < C and graph[dx][dy] == ".":
                addWater.append((dx, dy))
                graph[dx][dy] = "*"

    water = list(set(water) | set(addWater))


def bfs():

    Sx, Sy = S
    visited = [[False] * C for _ in range(R)]
    queue = deque()
    queue.append([Sx, Sy, 0])
    time = 0
    visited[Sx][Sy] = True
    
    while queue:
        x, y, c = queue.popleft()

        if time != c:
            changeWater()
            time = c

        if graph[x][y] == "D":
            return str(c)

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < R and 0 <= dy < C and not visited[dx][dy]:
                if graph[dx][dy] == "D":
                    return c + 1
                elif graph[dx][dy] == "." and check(dx, dy):
                    queue.append([dx, dy, c + 1])
                    visited[dx][dy] = True

    return "KAKTUS"

print(bfs())