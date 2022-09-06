import sys
sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visit = [[-1] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


def dfs(x, y):
    if x == n - 1 and y == m -1:
        return 1

    if visit[x][y] != -1:
        return visit[x][y]

    cnt = 0
    for move in moves:
        dx, dy = x + move[0], y + move[1]

        if 0 <= dx < n and 0 <= dy < m and graph[x][y] > graph[dx][dy]:
            cnt += dfs(dx, dy)

    visit[x][y] = cnt
    return visit[x][y]


print(dfs(0, 0))