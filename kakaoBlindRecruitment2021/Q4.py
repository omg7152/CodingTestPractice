# 플로이드 - 워셜 알고리즘으로 해결
from collections import deque
def solution(n, s, a, b, fares):
    answer = float('inf')

    # 전체 택시요금
    costs = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    # 자기자신 = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                costs[i][j] = 0

    # 주어진 조건에 따라 각 점까지의 택시 요금
    for x, y, z in fares:
        costs[x][y] = z
        costs[y][x] = z

    # start - k - end 로 거쳐갈 경우 최소값
    for k in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                costs[start][end] = min(costs[start][end], costs[start][k] + costs[k][end])

    # 각자 택시를 타고 갈 경우
    answer = min(answer, costs[s][a] + costs[s][b])
    # a 들렸다가 b로 갈 경우
    answer = min(answer, costs[s][b] + costs[b][a])
    # b 들렸다가 a로 갈 경우
    answer = min(answer, costs[s][a] + costs[a][b])

    # a, b 가 아니라 다른 지점에 도착 후 각자 택시를 탈 경우
    for i in range(1, n + 1):
        if i != s and i != a and i != b:
            answer = min(answer, costs[s][i] + costs[i][a] + costs[i][b])
    
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))