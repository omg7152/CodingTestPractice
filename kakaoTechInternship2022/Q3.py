from collections import deque

def solution(alp, cop, problems):

    # 목표 알고력과 코딩력
    max_alp = max([p[0] for p in problems])
    max_cop = max([p[1] for p in problems])

    # 초기 값에서 부터의 최단거리
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]

    #초기 알고력과 코딩력이 목표 알고력과 코딩력 보다 크면 초기 알고력과 코딩력을 목표 알고력과 코딩력으로 변경
    alp = max_alp if alp > max_alp else alp
    cop = max_cop if cop > max_cop else cop

    queue = deque()
    queue.append([alp, cop])
    dp[alp][cop] = 0

    while queue:
        a, c = queue.popleft()


        if a + 1 <= max_alp and dp[a + 1][c] > dp[a][c] + 1:
            queue.append([a + 1, c,])
            dp[a + 1][c] = dp[a][c] + 1

        if c + 1 <= max_cop and dp[a][c + 1] > dp[a][c] + 1:
            queue.append([a, c + 1])
            dp[a][c + 1] = dp[a][c] + 1

        for p in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = p

            if a >= alp_req and c >= cop_req:

                # 각 알고력과 코딩력이 목표 알고력과 코딩력 보다 크면 목표 알고력과 코딩력으로 변경
                next_alp = a + alp_rwd if a + alp_rwd <= max_alp else max_alp
                next_cop = c + cop_rwd if c + cop_rwd <= max_cop else max_cop

                if dp[next_alp][next_cop] > dp[a][c] + cost:
                    queue.append([next_alp, next_cop])
                    dp[next_alp][next_cop] = dp[a][c] + cost

    return dp[max_alp][max_cop]

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))