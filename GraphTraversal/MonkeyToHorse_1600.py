import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0, K])

    while queue:
        x, y, k =  queue.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][k]

        # 일반이동
        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < H and 0 <= dy < W and graph[dx][dy] != 1 and visited[dx][dy][k] == 0:
                visited[dx][dy][k] = visited[x][y][k] + 1
                queue.append([dx, dy, k])
        
        #말이동
        if k > 0:
            for move in movesHorse:
                dx, dy = x + move[0], y + move[1]

                if 0 <= dx < H and 0 <= dy < W and graph[dx][dy] != 1 and visited[dx][dy][k - 1] == 0:
                    visited[dx][dy][k - 1] = visited[x][y][k] + 1
                    queue.append([dx, dy, k - 1])
    
    return -1

K = int(sys.stdin.readline().rstrip())
W, H = map(int, sys.stdin.readline().rstrip().split())
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
movesHorse = [[1, 2], [2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1], [1, -2], [-2, 1]]
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
graph = []
for _ in range(H):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(bfs())

