import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

root = [-1] * 101
visited = [False] * 101

for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    root[a] = b

queue = deque()
queue.append([1, 0])
visited[1] = True

while queue:
    x, cnt = queue.popleft()

    if x == 100:
        print(cnt)
        break

    for i in range(1, 7):
        if x + i <= 100:
            dx = x + i if root[x + i] == -1 else root[x + i]

            if not visited[dx]:
                visited[dx] = True
                queue.append([dx, cnt + 1])
