def dfs(idx, graph, dp, sales):
    # 리프노드 
    if not graph[idx]:
        # 현재노드 참석 최소 매출액을 현재노드의 매출액으로 변경
        dp[idx][1] = sales[idx - 1]
        return

    # 자식노드 매출액 최소값의 합
    sum_child = 0
    # 미참석 매출액이 참석 매출액보다 큰 자식노드가 있는지 체크
    check = False
    # 자식노드의 참석 매출액 - 미참석 매출액 의 최소값
    diff = float('inf')

    for next in graph[idx]:
        dfs(next, graph, dp, sales)

        sum_child += min(dp[next][0], dp[next][1])

        if dp[next][0] > dp[next][1]:
            check = True
        else:
            diff = min(diff, dp[next][1] - dp[next][0])

    # 현재노드 참석 매출액 = 현재노드 매출 + 자식노드 매출액 최소값합
    dp[idx][1] = sales[idx - 1] + sum_child

    # 자식노드의 미참석 매출액이 참석 매출액보다 크다면 해당 그룹의 한명이 이미 참석함
    if check:
        dp[idx][0] = sum_child

    # 아직 참석한 인원이 그룹 안에 없기 떄문에 자식노드의 매출액이 최소인 노드를 참석 시킴
    else:
        dp[idx][0] = sum_child + diff

def solution(sales, links):
    answer = 0

    n = len(sales)
    # [미참석 매출액, 참석 매출액]
    dp = [[0, 0] for _ in range(n + 1)]

    graph = [[] for _ in range(n + 1)]

    for a, b in links:
        graph[a].append(b)

    dfs(1, graph, dp, sales)

    # CEO 노드의 최소 매출액
    answer = min(dp[1][0], dp[1][1])

    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(solution([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]))