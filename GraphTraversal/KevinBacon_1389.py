import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

INF = float('inf')
distences = [[INF] * (N + 1) for _ in range(N + 1)]
graph = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph.append([a, b, 1])
    graph.append([b, a, 1])

for i in range(1, N + 1):
    distences[i][i] = 0

for a, b, c in graph:
    distences[a][b] = min(distences[a][b], c)

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            distences[a][b] = min(distences[a][b], distences[a][k] + distences[k][b])

minCnt = INF
result = 0

for i in range(1, N + 1):
    temp = sum(distences[i][1:])

    if minCnt > temp:
        result = i
        minCnt = temp

print(result)
