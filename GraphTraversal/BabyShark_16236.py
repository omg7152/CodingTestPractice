import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = []
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#상어의 현재 위치
sharkX, sharkY, sharkSize = 0, 0, 2

for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        #상어의 위치 저장
        if temp[j] == 9:
            temp[j] = 0
            sharkX, sharkY = i, j
            break
    graph.append(temp)

#먹을 수 있는 물고기 찾기
def eatAbleFishList():
    queue = deque()
    visit = [[False] * N for _ in range(N)]

    queue.append([sharkX, sharkY, 0])
    visit[sharkX][sharkY] = True

    #먹을 수 있는 물고기의 좌표, 물고기까지 이동거리 저장하는 리스트
    result = []

    while queue:
        x, y, z = queue.popleft()

        for move in moves:
            dx, dy = x + move[0], y + move[1]

            if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] <= sharkSize and visit[dx][dy] == False:
                visit[dx][dy] = True
                queue.append([dx, dy, z + 1])

                #물고기의 크기가 상어의 크기보다 작으면 저장
                if 0 < graph[dx][dy] < sharkSize:
                    result.append([dx, dy, z + 1])

    #이동거리가 가장 작고, 가장 위에 있고, 가장 왼쪽에 있는 순으로 오름차순 정렬
    return sorted(result, key = lambda x : (x[2], x[0], x[1]))
 
eatFishCnt = 0
TotalDistence = 0
while True:

    eatAbleFishs = eatAbleFishList()

    #먹을수 있는 물고기가 없으면 총 이동거리 출력
    if not eatAbleFishs:
        print(TotalDistence)
        break

    #먹을 수 있는 물고기중 조건에 맞는 가장 첫번째 물고기 먹음
    x, y, distence = eatAbleFishs[0]

    #현재 상어의 위치 변경
    sharkX, sharkY = x, y
    #총 이동거리 증가
    TotalDistence += distence
    #먹은 물고기 수 증가
    eatFishCnt += 1
    #물고기 먹은 처리
    graph[x][y] = 0

    #상어의 크기만큼 물고기를 먹었다면 상어 사이즈 키워주고 먹은 물고기 수 초기화
    if eatFishCnt == sharkSize:
        sharkSize += 1
        eatFishCnt = 0
