import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([A, ""])
    visited = [False] * 10000

    while queue:
        a, cmd = queue.popleft()

        if B == a:
            print(cmd)
            break
        
        a2 = (2 * a) % 10000
        if not visited[a2]:
            queue.append([a2, cmd + "D"])
            visited[a2] = True
        
        a2 = (a - 1) % 10000
        if not visited[a2]:
            queue.append([a2, cmd + "S"])
            visited[a2] = True

        a2 = (a * 10 + (a // 1000)) % 10000
        if not visited[a2]:
            queue.append([a2, cmd + "L"])
            visited[a2] = True
        
        a2 = (a // 10 + ((a % 10) * 1000)) % 10000
        if not visited[a2]:
            queue.append([a2, cmd + "R"])
            visited[a2] = True


T = int(sys.stdin.readline().rstrip())
case = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    case.append([a, b])

for A, B in case:
    bfs()