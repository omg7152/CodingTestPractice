import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque()
queue.append([N, str(N) + " "])
visited = [-1] * 1000001
visited[N] = 0

while queue:
    x, root = queue.popleft()

    if x == 1:
        print(visited[x])
        print(root)
        break

    if x % 3 == 0 and visited[x // 3] == -1:
        queue.append([x // 3, root + str(x // 3) + " "])
        visited[x // 3] = visited[x] + 1

    if x % 2 == 0 and visited[x // 2] == -1:
        queue.append([x // 2, root + str(x // 2) + " "])
        visited[x // 2] = visited[x] + 1

    if 0 < x - 1 < 1000001 and visited[x - 1] == -1:
        queue.append([x - 1, root + str(x - 1) + " "])
        visited[x - 1] = visited[x] + 1

