# 위상정렬 : 순서가 정해져있는 작업을 차례로 수행해야 할 떄 그 순서를 결정해주기 위해 사용하는 알고리즘

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

# 각 정점에 자식으로 연결된 정점 리스트
graph = [[] for _ in range(n + 1)]
# 진입 차수(각 정점에 들어오는 간선의 수)
indegree = [0] * (n + 1)
queue = deque()
result = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    graph[a].append(b)
    indegree[b] += 1

# 진입 차수가 0 인 정점 큐에 추가
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

for i in range(n):
    # 큐에서 값 꺼냄
    x = queue.popleft()

    # 꺼낸 값 결과 리스트에 추가
    result.append(x)

    # 꺼낸 정점의 자식으로 연결된 점의 진입차수를 1감소하고 진입차수가 0 이라면 큐에 추가
    for j in graph[x]:
        indegree[j] -= 1

        if indegree[j] == 0:
            queue.append(j)

print(' '.join(str(i) for i in result))