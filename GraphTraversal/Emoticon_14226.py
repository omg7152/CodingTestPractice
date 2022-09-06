import sys
from collections import deque

s = int(sys.stdin.readline().rstrip())
visited = [[False] * (s + 1) for _ in range(s + 1)]
queue = deque()
queue.append([1, 0, 0])
visited[1][0] = 0

while queue:
    window, clip, time = queue.popleft()

    if window == s:
        print(time)
        break

    if not visited[window][window]:
        queue.append([window, window, time + 1])
        visited[window][window] = True

    if window - 1 > 0 and not visited[window - 1][clip]:
        queue.append([window - 1, clip, time + 1])
        visited[window - 1][clip] = True
    
    if window + clip <= s and not visited[window + clip][clip]:
        queue.append([window + clip, clip, time + 1])
        visited[window + clip][clip] = True
