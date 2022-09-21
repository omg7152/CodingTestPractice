from collections import deque

def solution(board):
    answer = 0

    n = len(board)

    visit = [[[[False for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    queue = deque()
    queue.append([0, 0, 0, 1, 0, 0])
    visit[0][0][0][1] = True
    visit[0][1][0][0] = True
 

    while queue:
        x1, y1, x2, y2, direction, count = queue.popleft()

        if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
            answer = count
            break

        # 상하좌우
        for move in moves:
            dx1, dy1, dx2, dy2 = x1 + move[0], y1 + move[1], x2 + move[0], y2 + move[1]

            if 0 <= dx1 < n and 0 <= dy1 < n and 0 <= dx2 < n and 0 <= dy2 < n and not visit[dx1][dy1][dx2][dy2]:
                if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
                    visit[dx1][dy1][dx2][dy2] = True
                    visit[dy2][dx2][dx1][dy1] = True
                    queue.append([dx1, dy1, dx2, dy2, direction, count + 1])

        # 회전
        for spin in [-1, 1]:
            dx1, dy1, dx2, dy2 = 0, 0, 0, 0
            if direction == 0:
                dx1, dy1, dx2, dy2 = x1 + spin, y1, x2 + spin, y2
            else:
                dx1, dy1, dx2, dy2 = x1, y1 + spin, x2, y2 + spin

            if 0 <= dx1 < n and 0 <= dy1 < n and 0 <= dx2 < n and 0 <= dy2 < n:
                if board[dx1][dy1] == 0 and board[dx2][dy2] == 0:
                    if not visit[x1][y1][dx1][dy1]:
                        visit[x1][y1][dx1][dy1] = True
                        visit[dx1][dy1][x1][y1] = True
                        queue.append([x1, y1, dx1, dy1, direction ^ 1, count + 1])

                    if not visit[x2][y2][dx2][dy2]:
                        visit[x2][y2][dx2][dy2] = True
                        visit[dx2][dy2][x2][y2] = True
                        queue.append([x2, y2, dx2, dy2, direction ^ 1, count + 1])

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))# 21
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))# 11
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))# 33
print(solution([[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))# 10
print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))# 18