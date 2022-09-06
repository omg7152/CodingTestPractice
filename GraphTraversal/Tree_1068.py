import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = list(map(int, sys.stdin.readline().rstrip().split()))
childGraph = [[] for _ in range(N)]

rootNode = -1

for i in range(N):
    if graph[i] == -1:
        rootNode = i
    else:
        childGraph[graph[i]].append(i)


removeNode = int(sys.stdin.readline().rstrip())

queue = deque()
queue.append(rootNode)
ans = 0

while queue:
    node = queue.popleft()

    if node == removeNode:
        continue

    cnt = 0

    for i in childGraph[node]:
        if i != removeNode:
            cnt += 1
            queue.append(i)

    if cnt == 0:
        ans += 1

print(ans)
