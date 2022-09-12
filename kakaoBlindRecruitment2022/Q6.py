# 범위 체크 하여 그래프 수정 시 각 좌표별로 수정하면 시간초과가 나와기 때문에 
# 가로합 세로합 하여 변경될 수치 체크하여 변경 여부 구하여 해결
# 0 에서 4까지 있는 그래프 중 0 ~ 2 까지 3만큼 변경한다면
# 3 0 0 -3 0 이와 같이 체크하고 가로합(0 부터 자기자신 좌표까지 전부 더한값) 을 하면 3 3 3 3 0 0 으로 나타낼 수 있다

def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])

    change = [[0] * (m + 1) for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skill:

        # 각 좌표에 degree값 알맞게 저장 
        # (r1, c1), (r2 + 1, c2 + 1) -> 가로합 세로 합 구하기 위해 1씩 증가 시켜 저장
        change[r1][c1] += degree if type == 2 else -degree
        change[r1][c2 + 1] += -degree if type == 2 else degree
        change[r2 + 1][c1] += -degree if type == 2 else degree
        change[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 세로합 
    for i in range(n):
        for j in range(m):
                change[i + 1][j] += change[i][j]
    # 가로합
    for i in range(n):
        for j in range(m):
                change[i][j + 1] += change[i][j]
                
    for i in range(n):
        for j in range(m):
            board[i][j] += change[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))