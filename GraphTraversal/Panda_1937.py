import sys
sys.setrecursionlimit(10 ** 7)

def dfs(x, y):

    if moveCnt[x][y] != -1:
        return moveCnt[x][y]

    cnt = 0
    for move in moves:
        dx, dy = x + move[0], y + move[1]

        if 0 <= dx < N and 0 <= dy < N and graph[x][y] < graph[dx][dy]:
            cnt = max(cnt, dfs(dx, dy))

    moveCnt[x][y] = cnt + 1
    return cnt + 1

        

N = int(sys.stdin.readline().rstrip())

moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
moveCnt = [[-1] * N for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

ans = 0
for i in range(N):
    for j in range(N):
        if moveCnt[i][j] == -1:
            ans = max(ans, dfs(i, j))
        else:
            ans = max(ans, moveCnt[i][j])

print(ans)