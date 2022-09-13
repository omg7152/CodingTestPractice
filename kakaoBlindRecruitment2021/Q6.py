from collections import deque
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Ctrl 이동
def moveCtrl(x, y, cmd, board):
    # 오른쪽으로 이동
    if cmd == 0:
        for i in range(y + 1, 4):
            if board[x][i] != 0:
                return x, i
        return x, 3

    # 아래로 이동
    elif cmd == 1:
        for i in range(x + 1, 4):
            if board[i][y] != 0:
                return i, y
        return 3, y
    
    # 왼쪽으로 이동
    elif cmd == 2:
        for i in range(y - 1, -1, -1):
            if board[x][i] != 0:
                return x, i
        return x, 0

    # 위로 이동
    else:
        for i in range(x - 1, -1, -1):
            if board[i][y] != 0:
                return i, y
        return 0, y

# 현재 카드와 같은 카드 좌표 조회
def getSameCard(x, y, board):
    for i in range(4):
        for j in range(4):
            if (x != i or y != j) and board[i][j] == board[x][y]:
                return i, j

    return -1, -1

# 현재 좌표에서 가장 가까운 카드 조회
def getNearCard(x, y, board):
    result = []
    min_dist = float('inf')

    for i in range(4):
        for j in range(4):
            if (i != x or j != y) and board[i][j] != 0:
                dist = getShortDist(x, y, i, j, board)
                if min_dist > dist:
                    min_dist = dist
                    result = [[i, j]]
                elif min_dist == dist:
                    result.append([i, j])

    return result, min_dist

# 시작 좌표에서 끝좌표까지 가장 적게 이동하는 횟수 조회
def getShortDist(x, y, nx, ny, board):
    visited = [[float('inf')] * 4 for _ in range(4)]
    queue = deque()
    queue.append([x, y, 0])

    while queue:
        curr_x, curr_y, curr_dist = queue.popleft()

        if curr_x == nx and curr_y == ny:
            continue

        for move in moves:
            dx, dy = curr_x + move[0], curr_y + move[1]

            if 0 <= dx < 4 and 0 <= dy < 4 and visited[dx][dy] > curr_dist + 1:
                visited[dx][dy] = curr_dist + 1
                queue.append([dx, dy, curr_dist + 1])

        for i in range(4):
            dx, dy = moveCtrl(curr_x, curr_y, i, board)
            if (dx != curr_x or dy != curr_y) and visited[dx][dy] > curr_dist + 1:
                visited[dx][dy] = curr_dist + 1
                queue.append([dx, dy, curr_dist + 1])

    return visited[nx][ny]

def solution(board, r, c):
    answer = float('inf')

    queue = deque()
    queue.append([r, c, 0, board])

    while queue:
        x, y, count, curr_board = queue.popleft()

        # 현재좌표가 카드일경우
        if curr_board[x][y] != 0:
            # 같은 카드의 좌표 조회
            nx, ny = getSameCard(x, y, curr_board)
            # 현재 위치부터 같은 카드의 위치까지 가장 작은 이동 횟수 조회
            dist = getShortDist(x, y, nx, ny, curr_board)
            # 보드 복사
            next_board = [[j for j in i] for i in curr_board]
            # 해결된 카드 삭제
            next_board[x][y] = 0
            next_board[nx][ny] = 0
            queue.append([nx, ny, count + dist + 2, next_board])

        # 현재좌표가 카드가 아닐경우
        else:
            # 가장 가까운 카드 리스트와 이동 횟수 조회
            cardList, dist = getNearCard(x, y, curr_board)

            # 카드가 없을경우 이동 횟수 비교하여 저장
            if not cardList:
                answer = min(answer, count)
            else:
                # 가장 가까운 카드 큐에 저장
                for nx, ny in cardList:
                    next_board = [[j for j in i] for i in curr_board]
                    queue.append([nx, ny, count + dist, next_board])

    return answer

print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
