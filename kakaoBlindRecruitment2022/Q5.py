max_sheep = 0
def dfs(node, sheep, wolf, group, graph, info):
    global max_sheep
    sheep += info[node] ^ 1
    wolf += info[node]

    if sheep <= wolf:
        return
    else:
        max_sheep = max(max_sheep, sheep)
        next_group = group | set(graph[node])

    for next_node in next_group:
        dfs(next_node, sheep, wolf, next_group - set([next_node]), graph, info)
    

def solution(info, edges):
    global max_sheep
    graph = [[] for _ in range(len(info))]

    for a, b in edges:
        graph[a].append(b)

    dfs(0, 0, 0, set([]), graph, info)

    return max_sheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))