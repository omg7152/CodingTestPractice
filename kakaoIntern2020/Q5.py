cnt = 1

def dfs(graph, visited, req, curr):
    global cnt

    if not visited[curr]:
        cnt += 1
        temp += 1
        visited[curr] = True

    temp = 0
    for next in graph[curr]:
        if req[next] == -1 or (req[next] != -1 and visited[req[next]]):
            dfs(graph, visited, req, curr)

    

def solution(n, path, order):
    answer = True

    visited = [False] * n
    req = [-1] * n
    for a, b in order:
        req[b] = a

    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)

    
    while cnt < n - 1:

        if dfs(graph, visited, req, 0) == 0:
            answer = False
            break
    

    return answer

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))