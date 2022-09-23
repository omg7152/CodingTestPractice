from collections import defaultdict

def solution(board):
    answer = 0

    group = {}
    remain = defaultdict(list)

    # 각 그룹별 직사각형 범위 체크
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                if board[i][j] not in group:
                    group[board[i][j]] = [[float('inf'), float('inf')], [-1, -1]]

                group[board[i][j]][0][0] = min(group[board[i][j]][0][0], i)
                group[board[i][j]][0][1] = min(group[board[i][j]][0][1], j)
                group[board[i][j]][1][0] = max(group[board[i][j]][1][0], i)
                group[board[i][j]][1][1] = max(group[board[i][j]][1][1], j)

    
    for key in group:
        minX, minY = group[key][0]
        maxX, maxY = group[key][1]

        # 각 그룹의 직사각형 범위에서 아직 채워지지 않은 좌표 저장
        for i in range(minX, maxX + 1):
            for j in range(minY, maxY + 1):
                if board[i][j] != key:
                    remain[key].append([i, j])
        # 채워지지 않은 두 직사각형의 x좌표 거리가 1 보다 크면 ㅓ, ㅏ 모양으로 제거 불가하기 때문에 dict에서 제거
        if abs(remain[key][0][0] - remain[key][1][0]) > 1:
            del remain[key]
        # 그룹의 직사각형 범위중 가장 위에 칸이 전부 채워져 있고 채워지지 않은 부분이 전부 아래쪽일 경우 제거 불가
        elif minX < remain[key][0][0] and minX < remain[key][1][0]:
            del remain[key]

    # 제거 가능한 그룹 중 상단에 제거 불가능한 그룹이 있으면 해당 그룹도 제거 불가
    while True:
        delList = []
        for key in remain:
            x1, y1 = remain[key][0]
            x2, y2 = remain[key][1]
            temp1 = [board[i][y1] for i in range(x1 + 1)]
            temp2 = [board[i][y2] for i in range(x2 + 1)]
            for key2 in group:
                if key2 not in remain:
                    if key2 in temp1 or key2 in temp2:
                        delList.append(key)
                        break
        if len(delList) == 0:
            break
        else:
            for k in delList:
                del remain[k]

    answer = len(remain)
    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))