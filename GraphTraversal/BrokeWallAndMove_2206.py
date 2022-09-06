import sys
from collections import deque
N, M = list(map(int, sys.stdin.readline().rstrip().split()))
graph = []
moves = [[1,0],[-1,0],[0,1],[0,-1]]

#각 칸까지의 이동거리 리스트(벽을 부수지 않았을때와 벽을 부쉈을떄 의 원소를 가진다)
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs():
    queue = deque()
    queue.append([0, 0 ,0])
    visited[0][0][0] = 1
    while queue:
        # z => 벽을 부셨는지 여부 (0 -> 벽 부수지 않음, 1 -> 벽을 부숨)
        x, y, z= queue.popleft() #현재칸

        # 마지막 도착하면 리턴
        if x == N - 1 and y == M -1:
            return visited[x][y][z]

        for move in moves:
            #이동할 칸의 좌표
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < N and 0 <= dy < M:
                #이동 가능하고 아직 방문하지 않았다면
                if graph[dx][dy] == 0 and visited[dx][dy][z] == 0:
                    #이동할 칸의 이동거리를 현재칸의까지의 이동거리 + 1 로 수정(벽을 부순여부는 현재칸과 동일)
                    visited[dx][dy][z] = visited[x][y][z] + 1
                    queue.append([dx, dy, z])
                #이동할 위치가 벽이고 벽을 아직 부수지 않았을경우
                elif graph[dx][dy] == 1 and z == 0:
                    #이동할 칸의 벽을 부쉈을때 해당칸까지 이동거리를 현재 칸까지 이동거리 + 1 로 수정
                    visited[dx][dy][1] = visited[x][y][z] + 1
                    # 다음 탐색부터 벽을 부쉈는지 여부를 벽을 부순상태로 큐에 추가
                    queue.append([dx, dy, 1])
    return -1

print(bfs())