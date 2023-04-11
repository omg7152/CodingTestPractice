import sys
sys.setrecursionlimit(10 ** 7)

def dfs(start, dist):
    for next_node, next_dist in graph[start]:
        if distence[next_node] == -1:
            distence[next_node] = dist + next_dist
            dfs(next_node, dist + next_dist)


n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

distence = [-1] * (n + 1)
distence[1] = 0
dfs(1, 0)

start = distence.index(max(distence))
distence = [-1] * (n + 1)
distence[start] = 0
dfs(start, 0)

print(max(distence))
