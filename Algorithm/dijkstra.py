#다익스트라 알고리즘 : 하나의 시작 정점으로 부터 모든 다른 정점까지의 최단 경로를 찾는 최단 경로 알고리즘
#시간복잡도 = O(ElogV) (E : 간선의 개수, V : 노드의 개수)
import heapq
INF = float('inf')

graph = [
    [[1, 8], [2, 1], [3, 2]],
    [],
    [[1, 5], [3, 2]],
    [[4, 3], [5, 5]],
    [[5, 1]],
    [[0, 5]]
]

def dijkstra(start):
    # 최단거리를 저장하기 위한 리스트
    distances = [INF for _ in range(len(graph))]
    #시작값은 0
    distances[start] = 0 
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        #저장된 거리보다 크면 건너뜀
        if distances[curr_node] < curr_dist:  
            continue
    
        for next_node, next_dist in graph[curr_node]:
            distance = curr_dist + next_dist

            #저장된 거리보다 작으면 변경
            if distance < distances[next_node]:  
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])
        
    return distances

print(dijkstra(0))