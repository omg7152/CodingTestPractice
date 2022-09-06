import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
chicken = []
homes = []
result = float('inf')

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append([i, j])
        if graph[i][j] == 2:
            chicken.append([i, j])

for selchicken in combinations(chicken, m):
    temp = 0
    for home in homes:
        xh, yh = home
        dis = float('inf')
        for i in range(m):
            dis = min(dis, abs(xh - selchicken[i][0]) + abs(yh - selchicken[i][1]))
        temp += dis
    result = min(result, temp)

print(result)
