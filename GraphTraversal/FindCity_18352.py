import sys
import heapq

def dijkstra(start):
    distence = [float('inf') for _ in range(n + 1)]
    distence[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if distence[curr_node] < curr_dist:
            continue

        for next_node in graph[curr_node]:
            dist = curr_dist + 1

            if distence[next_node] > dist:
                distence[next_node] = dist
                heapq.heappush(queue, [dist, next_node])

    cnt = 0
    for i in range(1, n +1):
        if distence[i] == k:
            cnt += 1
            print(i)
    
    if cnt == 0:
        print(-1)


n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

dijkstra(x)

