import sys
from collections import deque

def moveFire():
    global fire
    newFire = deque()
    while fire:
        x, y = fire.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < h and 0 <= dy < w and graph[dx][dy] == ".":
                newFire.append([dx, dy])
                graph[dx][dy] = "*"
    
    fire = newFire

def moveSang():
    global sang
    newSang = deque()
    while sang:
        x, y = sang.popleft()

        if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            return 2

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < h and 0 <= dy < w and graph[dx][dy] == "." and not visited[dx][dy]:
                newSang.append([dx, dy])
                visited[dx][dy] = True

    if newSang:
        sang = newSang
        return 0
    else:
        return 1


t = int(sys.stdin.readline().rstrip())
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(t):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for i in range(h):
        graph.append(list(sys.stdin.readline().rstrip()))

    fire = deque()
    sang = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire.append([i, j])
            elif graph[i][j] == "@":
                sang.append([i, j])
                graph[i][j] = "."
                visited[i][j] = True

    ans = 0         
    while True:
        moveFire()
        check = moveSang()
        ans += 1
        if check == 2:
            print(ans)
            break
        elif check == 1:
            print("IMPOSSIBLE")
            break
        

    