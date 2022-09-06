import sys

n, m = int(sys.stdin.readline().rstrip()), int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

ans = set([])
for i in graph[1]:
    for j in graph[i]:
        if j != 1 and j != i:
            ans.add(j)
    ans.add(i)

print(len(ans))