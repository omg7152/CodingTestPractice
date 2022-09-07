from collections import defaultdict

def solution(n, path, order):

    # 노드를 방문하기 전 필수로 방문해야 하는 노드
    require = defaultdict(int)
    # 노드 연결 정보
    graph = [[] for _ in range(n)]
    # 노드 방문 정보
    visited = [False] * n
    # 필수로 방문해야하는 노드를 방문하지 않아 다른 노드 방문 후 다시 방문해야 하는 노드
    re = defaultdict(int)
    stack = [0]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in order:
        # 0번 노드를 방문하기전에 필수로 방문해야하는 노드가 있으면 False 리턴
        if b == 0:
            return False
        require[b] = a


    while stack:
        node = stack.pop()

        if node in require and not visited[require[node]]:
            re[require[node]] = node
            continue

        # 방문처리
        visited[node] = True

        for next_node in graph[node]:
            if not visited[next_node]:
                stack.append(next_node)

        # 현재노드 방문 후 재방문 해야하는 노드가 있으면 stack에 추가
        if node in re:
            stack.append(re[node])


    return False not in visited

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	, [[4,1],[8,7],[6,5]]))