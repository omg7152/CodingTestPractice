import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split())

visited = [False] * (F + 1)
queue = deque()
queue.append([S, 0])
visited[S] = True


result = "use the stairs"


while queue:
    curr_floor, curr_dist = queue.popleft()

    if curr_floor == G:
        result = str(curr_dist)
        break

    for i in [U, D * -1]:
        next_floor = curr_floor + i

        if 0 < next_floor <= F and not visited[next_floor]:
            queue.append([next_floor, curr_dist + 1])
            visited[next_floor] = True

print(result)