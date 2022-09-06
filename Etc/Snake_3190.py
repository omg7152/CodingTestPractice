import sys
from collections import deque
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

graph = [[0] * n for _ in range(n)]

direction = deque()
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake = deque()

for i in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    graph[x - 1][y - 1] = 1


l = int(sys.stdin.readline().rstrip())

for i in range(l):
    direction.append(list(map(str, sys.stdin.readline().rstrip().split())))

dtime, dire = direction.popleft()

def moveSnake(x, y, time, d):
    global dtime, dire
    # 현재위치가 벽 또는 뱀 자신일경우 종료
    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 2:
        return time

    # 현재 칸에 사과가 없고 뱀 큐가 있을경우
    if graph[x][y] != 1 and snake:
        # 뱀 큐에서 가장처음 좌표를 추출
        sx, sy = snake.popleft()
        # 해당 좌표를 빈칸으로 수정
        graph[sx][sy] = 0

    # 그래프에서 현재 좌표를 뱀이 있는 처리
    graph[x][y] = 2
    # 전체 뱀의 좌표에 현재 좌표 추가
    snake.append([x, y])

    # 현재 시간과 방향변경시간이 같을경우
    if time == int(dtime):
        # 왼쪽
        if dire == 'L':
            d = d - 1 if d > 0 else 3
        # 오른쪽
        else:
            d = d + 1 if d < 3 else 0
        
        # 아직 변경할 방향이 남아있으면 큐애서 꺼내어 변수에 저장
        if direction:
            dtime, dire = direction.popleft()


    return moveSnake(x + moves[d][0], y + moves[d][1], time + 1, d)

print(moveSnake(0, 0, 0, 0))