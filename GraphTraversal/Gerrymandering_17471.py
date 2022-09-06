import sys

def select(n, cnt, limit, p):
    if cnt == limit:
        global ans
        ans = min(ans, abs((total - p) - p))
        return

    for num in graph[n]:
        visited[num] = True
        select(num, cnt + 1, limit, p + people[num])
        visited[num] = False
        

n = int(sys.stdin.readline().rstrip())

people = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
visited = [False] * (n + 1)
graph = [[]]

for i in range(1, n + 1):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split()))[1:])

total = sum(people)
ans = total

for i in range(1, n + 1):
    for j in range(1, n + 1):
        visited[j] = True
        select(j, 1, i, people[i])
        visited[j] = False


