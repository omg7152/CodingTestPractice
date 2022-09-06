import sys

graph = []
zero = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append([i, j])

def checkX(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkY(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkSQ(x, y, a):
    Xg, Yg = (x // 3) * 3, (y // 3) * 3

    for i in range(Xg, Xg + 3):
        for j in range(Yg, Yg + 3):
            if a == graph[i][j]:
                return False
    return True
        

def dfs(idx):
    if idx == len(zero):
        for i in range(9):
            print(' '.join(str(x) for x in graph[i]))
        exit(0)

    x, y = zero[idx]

    for a in range(1, 10):
        if checkX(x, a) and checkY(y, a) and checkSQ(x, y, a):
            graph[x][y] = a
            dfs(idx + 1)
            graph[x][y] = 0

dfs(0)