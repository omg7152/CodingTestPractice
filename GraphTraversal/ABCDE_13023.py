import sys

def dfs(x, cnt):
    if cnt == 5:
        return True

    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            if dfs(nx, cnt + 1):
                return True
            visited[nx] = False
    
    return False
    
n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited[i] = True
    if dfs(i, 1):
        print(1)
        break
    visited[i] = False
else:
    print(0)