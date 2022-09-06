import math
import sys
from collections import deque

def check(num):
    for i in range(2, math.trunc(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def bfs():
    queue = deque()
    visited = [False] * 10000
    queue.append([a, 0])
    visited[a] = True

    while queue:
        x, cnt = queue.popleft()

        if x == b:
            print(cnt)
            break

        for i in range(4):
            start = 0
            if i == 3:
                start = 1
            
            for j in range(start, 10):
                temp = x % (10 ** i) + (x // (10 ** (i + 1)) * (10 ** (i + 1))) + (j * (10 ** i))

                if not visited[temp] and check(temp):
                    queue.append([temp, cnt + 1])
                    visited[temp] = True
    else:
        print("Impossible")

t = int(sys.stdin.readline().rstrip())
case = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(t)]

for a, b in case:
    bfs()
