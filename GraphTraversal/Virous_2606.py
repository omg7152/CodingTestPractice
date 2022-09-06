import sys;

N = int(sys.stdin.readline().rstrip());
M = int(sys.stdin.readline().rstrip());
graph = [[] for _ in range(N + 1)];
visited = [False for _ in range(N + 1)];

for i in range(M):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()));
    graph[a].append(b);
    graph[b].append(a);

def dfs(num):
    visited[num] = True;
    for i in graph[num]:
        if not visited[i]:
            dfs(i);
dfs(1);
print(visited.count(True) - 1);
