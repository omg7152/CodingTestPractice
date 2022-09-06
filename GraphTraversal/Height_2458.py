import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

distences = [[0] * (n + 1) for _ in range(n + 1)]

for a, b in graph:
    distences[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if distences[a][b] == 0 and distences[a][k] == 1 and distences[k][b] == 1:
                distences[a][b] = 1

ans = 0
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        temp += distences[i][j] + distences[j][i]

    if temp == n - 1:
        ans += 1

print(ans)