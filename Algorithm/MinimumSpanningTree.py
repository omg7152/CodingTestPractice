# 최소 신장 트리(minimum spanning tree​)
# 전체 요소들을 연결할 때 사용한다. Kruskal 알고리즘, Prim 알고리즘이 있다.
# Kruskal알고리즘은 간선들을 정렬해야하기 때문에 간선이 적으면 Kruskal, 많으면 Prim을 선택한다.
import sys
import heapq

# # Kruskal
# # 1.간선들을 정렬
# # 2.간선이 잇는 두 정점의 root를 찾는다.
# # 3.다르다면 하나의 root를 바꾸어 연결 시켜준다.
v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(v + 1)]
lines = []

for i in range(e):
    lines.append(list(map(int, sys.stdin.readline().rstrip().split())))

lines.sort(key = lambda x : x[2])

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

ans = 0

for a, b, w in lines:
    if find(a) != find(b):
        union(a, b)
        ans += w

print(ans)


# Prim
# 1.임의의 정점을 선택
# 2.해당 정점에서 갈 수 있는 간선을 minheap에 넣는다.
# 3.최소값을 뽑아 해당 정점을 방문 안했다면 선택한다.
v, e = map(int, sys.stdin.readline().rstrip().split())
visit = [False] * (v + 1)
lines = [[] for _ in range(v + 1)]
heap = [[0, 1]]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    lines[a].append([c, b])
    lines[b].append([c, a])

ans = 0
cnt = 0
while heap:

    if cnt == v:
        break

    c, a = heapq.heappop(heap)

    if not visit[a]:
        visit[a] = True
        ans += c
        cnt += 1
        for i in lines[a]:
            heapq.heappush(heap, i)

print(ans)



