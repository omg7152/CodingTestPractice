n, m = 0, 0
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 해당 위치에서 이동 가능한 위치가 있는지 체크
def moveCheck(x, y, board):
    for move in moves:
        dx, dy = x + move[0], y + move[1]
        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 1:
            return True
    return False

# A 이동
def moveA(ax, ay, bx, by, total_move, board):
    global n, m, moves

    # 현재 위치에서 이동가능 한 지점이 없을경우
    if not moveCheck(ax, ay, board):
        # 패배, 이동거리 리턴
        return False, total_move

    # A와 B의 위치가 같을경우 
    if ax == bx and ay == by:
        # A가 이동하면 발판이 사라지기 떄문에 승리, 이동거리 + 1 리턴
        return True, total_move + 1

    # 현재 발판 사라짐 처리
    board[ax][ay] = 0
    result, win, lose = False, float('inf'), 0
    for move in moves:
        dx, dy = ax + move[0], ay + move[1]

        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 1:
            next_result, next_move_count = moveB(dx, dy, bx, by, total_move + 1, board)
            
            # 다음 B의 이동이 전부 패배면
            if not next_result:
                #승리 처리
                result = True
                # 승리했을 때의 이동거리의 최소값 저장
                win = min(win, next_move_count)
            else:
                # 패배했을 떄의 이동거리의 최대값 저장
                lose = max(lose, next_move_count)
    # 현재 발판 복구
    board[ax][ay] = 1

    # 최종 결과 값이 승리이면 승리했을 때 이동거리, 패배이면 패배했을 때 이동거리 리턴
    return result, win if result else lose
    
# B이동
def moveB(ax, ay, bx, by, total_move, board):
    global n, m, moves

    # 현재 위치에서 이동가능 한 지점이 없을경우
    if not moveCheck(bx, by, board):
        # 패배, 이동거리 리턴
        return False, total_move
    
    # A와 B의 위치가 같을경우 
    if ax == bx and ay == by:
        # B가 이동하면 발판이 사라지기 떄문에 
        # 승리, 이동거리 + 1 리턴
        return True, total_move + 1

    # 현재 발판 사라짐 처리
    board[bx][by] = 0
    result, win, lose = False, float('inf'), 0
    for move in moves:
        dx, dy = bx + move[0], by + move[1]

        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 1:

            next_result, next_move_count = moveA(ax, ay, dx, dy, total_move + 1, board)

            # 다음 A의 이동이 전부 패배면
            if not next_result:
                #승리 처리
                result = True
                # 승리했을 때의 이동거리의 최소값 저장
                win = min(win, next_move_count)
            else:
                # 패배했을 떄의 이동거리의 최대값 저장
                lose = max(lose, next_move_count)

    # 현재 발판 복구
    board[bx][by] = 1

    # 최종 결과 값이 승리이면 승리했을 때 이동거리, 패배이면 패배했을 때 이동거리 리턴
    return result, win if result else lose

def solution(board, aloc, bloc):
    global n, m

    n, m = len(board), len(board[0])
    result, result_move = moveA(aloc[0], aloc[1], bloc[0], bloc[1], 0, board)

    return result_move


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
print(solution([[1]], [0, 0], [0, 0]))