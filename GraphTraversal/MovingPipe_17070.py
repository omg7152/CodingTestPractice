import sys

N = int(sys.stdin.readline().rstrip())

graph = [[0] * N]
moves = [[0, 1], [1, 0], [1, 1]]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N + 1)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp[1][1] = [1, 0, 0]

for i in range(1, N + 1):
    for j in range(1, N):
        if i == j == 1:
            continue

        if graph[i][j] == 0:
            #가로 
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            #세로
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
            #대각선
            if graph[i - 1][j] == graph[i][j - 1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])

print(sum(dp[-1][-1]))

