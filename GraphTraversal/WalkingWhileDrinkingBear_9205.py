import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(start)
    visited = [False] * n

    while queue:
        x, y = queue.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return ans.append("happy")
            

        for i in range(n):
            if not visited[i] and abs(x - shop[i][0]) + abs(y - shop[i][1]) <= 1000:
                queue.append(shop[i])
                visited[i] = True

    ans.append("sad")


t = int(sys.stdin.readline().rstrip())
ans = []

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    shop = []
    for _ in range(n):
        shop.append(list(map(int, sys.stdin.readline().rstrip().split())))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    bfs()
    
print(*ans, sep="\n")
