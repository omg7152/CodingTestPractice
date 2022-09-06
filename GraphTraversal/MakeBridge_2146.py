import sys
from collections import deque

def checkGroup(i, j):
    queue = deque()
    queue.append([i, j])
    group[i][j] = g

    while queue:
        x, y = queue.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < n and 0 <= dy < n and group[dx][dy] == 0 and graph[dx][dy] == 1:
                group[dx][dy] = g
                queue.append([dx, dy])

def bfs():
    while q:
        x, y = q.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < n and 0 <= dy < n:
                if graph[dx][dy] == 1 and group[dx][dy] != i:
                    return group2[x][y] - 1
                elif graph[dx][dy] == 0 and group2[dx][dy] == 0:
                    q.append([dx, dy])
                    group2[dx][dy] = group2[x][y] + 1


n = int(sys.stdin.readline().rstrip())

graph = []
group = [[0] * n for _ in range(n)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


g = 1
for i in range(n):
    for j in range(n):
        if group[i][j] == 0 and graph[i][j] == 1:
            checkGroup(i, j)
            g += 1

result = float('inf')

for i in range(1, g):
    q = deque()
    group2 = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] == 1 and group[j][k] == i:
                q.append([j, k])
                group2[j][k] = 1

    result = min(result, bfs())

print(result)




# 각 섬의 끝 지점에서 다른 섬 까지 거리의 최소값 

# import sys
# from collections import deque

# def checkGroup(i, j):
#     queue = deque()
#     queue.append([i, j])
#     group[i][j] = g
#     temp = []

#     while queue:
#         x, y = queue.popleft()

#         endPoint = False
#         for move in moves:
#             dx, dy = x + move[0], y + move[1]

#             if 0 <= dx < n and 0 <= dy < n and group[dx][dy] == 0:
#                 if graph[dx][dy] == 1:
#                     group[dx][dy] = g
#                     queue.append([dx, dy])
#                 else:
#                     endPoint = True

#         if endPoint:
#             temp.append([x, y])
#     endland.append(temp)

# n = int(sys.stdin.readline().rstrip())

# graph = []
# group = [[0] * n for _ in range(n)]
# moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


# g = 0
# endland = [[]]
# for i in range(n):
#     for j in range(n):
#         if group[i][j] == 0 and graph[i][j] == 1:
#             g += 1
#             checkGroup(i, j)

# result = float('inf')

# for i in range(1, g):
#     for sx, sy in endland[i]:
#         for j in range(i + 1, g + 1):
#             for ex, ey in endland[j]:
#                 result = min(result, abs(sx - ex) + abs(sy - ey))

# print(result - 1)


