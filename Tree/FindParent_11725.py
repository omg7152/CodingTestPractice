import sys
sys.setrecursionlimit(10 ** 7)

def dfs(graph, parents, node):

    for next in graph[node]:
        if parents[next] == 0:
            parents[next] = node
            dfs(graph, parents, next)

n = int(sys.stdin.readline().rstrip())

parents = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)

parents[1] = -1
dfs(graph, parents, 1)

for i in range(2, n + 1):
    print(parents[i])