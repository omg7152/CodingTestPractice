import heapq
INF = float('inf')

def checkReverse(curr_node, next_node, curr_state, trap_idx):
    # False - 변경 X, True - 변경 O
    curr_reverse, next_reverse = False, False

    if curr_node in trap_idx:
        # 현재 상태와 해당 트랩 변경된 상태와 & 연산한 값이 0보다 크면 변경 된 상태
        curr_reverse = curr_state & (1 << trap_idx[curr_node]) > 0
    
    if next_node in trap_idx:
        # 현재 상태와 해당 트랩 변경된 상태와 & 연산한 값이 0보다 크면 변경 된 상태
        next_reverse = curr_state & (1 << trap_idx[next_node]) > 0

    return curr_reverse != next_reverse

def getNextState(next_node, curr_state, trap_idx):
    if next_node in trap_idx:
        return curr_state ^ (1 << trap_idx[next_node])
    return curr_state

def solution(n, start, end, roads, traps):
    answer = INF
    # 각 트랩노드 변경 상황 에 따라 다르게 체크 해야 함으로 2 ** len(traps) 추가
    distence = [[INF for _ in range(n + 1)] for _ in range(2 ** len(traps))]

    # 비트연산 하기위해 트랩의 인덱스 체크
    trap_idx = {v : i for i, v in enumerate(traps)}

    graph = [[] for _ in range(n + 1)]
    for a, b, c in roads:
        # 정방향(다음노드, 소요시간, 길 변경 여부)
        graph[a].append([b, c, False])
        # 역박향(다음노드, 소요시간, 길 변경 여부)
        graph[b].append([a, c, True])

    queue = []
    heapq.heappush(queue, [0, start, 0])
    distence[0][start] = 0

    while queue:
        curr_cost, curr_node, curr_state = heapq.heappop(queue)

        if curr_node == end:
            answer = min(answer, curr_cost)
            continue

        if curr_cost > distence[curr_state][curr_node]:
            continue

        for next_node, next_cost, next_reverse in graph[curr_node]:
            
            # 해당 경로의 방향이 현재 사애의 방향과 다르면 건너뜀
            if next_reverse != checkReverse(curr_node, next_node, curr_state, trap_idx):
                continue
            
            next_state = getNextState(next_node, curr_state, trap_idx)
            sum_cost = curr_cost + next_cost

            # 소요시간이 저장된 소요시간보다 크면 건너뜀
            if sum_cost > distence[next_state][next_node]:
                continue

            distence[next_state][next_node] = sum_cost
            heapq.heappush(queue, [sum_cost, next_node, next_state])

    return answer