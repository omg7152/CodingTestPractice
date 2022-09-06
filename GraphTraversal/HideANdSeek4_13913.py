import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
visited = [-1 for _ in range(100001)]

queue = deque()
queue.append([N, str(N) + " "])
visited[N] = 0

while queue:
    node, root = queue.popleft()

    if node == K:
        print(visited[node])
        print(root)
        break

    if 0 <= node - 1 < 100001 and visited[node - 1] == -1:
        queue.append([node - 1, root + str(node - 1) + " "])
        visited[node - 1] = visited[node] + 1
    
    if 0 <= node * 2 < 100001 and visited[node * 2] == -1:
        queue.append([node * 2, root + str(node * 2) + " "])
        visited[node * 2] = visited[node] + 1

    if 0 <= node + 1 < 100001 and visited[node + 1] == -1:
        queue.append([node + 1, root + str(node + 1) + " "])
        visited[node + 1] = visited[node] + 1