from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    answer = []

    queue = []
    node = [float('inf')] * (n + 1)

    for g in gates:
        heapq.heappush(queue, (0, g))
        node[g] = 0

    # 산봉우리에 포함되는 지 여부 체크할 때 리스트일 경우 O(N) 의 시간복잡도가 나오기 때문에 변경
    summits = set(summits)

    graph = defaultdict(list)

    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if curr_node in summits or node[curr_node] < curr_dist:
            continue

        for next_node, next_dist in graph[curr_node]:
            inten = max(curr_dist, next_dist)

            if inten < node[next_node]:
                node[next_node] = inten
                heapq.heappush(queue, (inten, next_node))

    for summit in summits:
        answer.append([summit, node[summit]])

    answer.sort(key=lambda x : (x[1], x[0]))        

    return answer[0]