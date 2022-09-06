# 플로이드-워셜 알고리즘 : 그래프에서 가능한 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘이다.
# 시간복잡도 = O(V ** 3) (v : 노드의 개수)

INF = float('inf')
n = 5
graph = [
    [1, 2, 2],
    [1, 3, 3],
    [1, 4, 1],
    [1, 5, 10],
    [2, 4, 2],
    [3, 4, 1],
    [3, 5, 1],
    [4, 5, 3],
    [3, 5, 10],
    [3, 1, 8],
    [1, 4, 2],
    [5, 1, 7],
    [3, 4, 2],
    [5, 2, 4]
]

distences = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distences[i][i] = 0

for E in graph:
    a, b, c = E
    distences[a][b] = min(distences[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distences[a][b] = min(distences[a][b], distences[a][k] + distences[k][b])


for i in range(1, n + 1):
    print(' '.join(str(i) for i in distences[i][1:]))

