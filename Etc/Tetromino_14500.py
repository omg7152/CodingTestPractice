import sys

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
visit = [[False] * m for i in range(n)]
result = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def dfs(x, y, idx, total):
    global result

    if result >= total + maxval * (3 - idx):
        return

    if idx == 3:
        result = max(result, total)
        return
    else:
        for move in moves:
            dx, dy = move[0] + x, move[1] + y

            if 0 <= dx < n and 0 <= dy < m and not visit[dx][dy]:
                if idx == 1:
                    visit[dx][dy] = True
                    dfs(x, y, idx + 1, total + graph[dx][dy])
                    visit[dx][dy] = False

                visit[dx][dy] = True
                dfs(dx, dy, idx + 1, total + graph[dx][dy])
                visit[dx][dy] = False


maxval = max(map(max, graph))

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visit[i][j] = False

print(result)