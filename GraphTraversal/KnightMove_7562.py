import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = []
moves = [[-1, -2],[-2, -1],[-2, 1],[-1, 2],[1, 2],[2, 1],[2, -1],[1, -2]]

for i in range(N):
    temp = []
    temp.append(int(sys.stdin.readline().rstrip()))
    for j in range(2):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    graph.append(temp)

def bfs(i):
    queue = deque()
    visit = [[False for _ in range(graph[i][0])] for _ in range(graph[i][0])]
    queue.append([graph[i][1][0], graph[i][1][1], 0])
    while queue:
        x, y, z = queue.popleft()
        visit[x][y] = True
        if x == graph[i][2][0] and y == graph[i][2][1]:
            return z

        for move in moves:
            dx, dy = x + move[0], y + move[1]
            
            if 0 <= dx < graph[i][0] and 0 <= dy < graph[i][0] and visit[dx][dy] == False:
                queue.append([dx, dy, z + 1])
                visit[dx][dy] = True
    return 0

for i in range(N):
    print(bfs(i))
