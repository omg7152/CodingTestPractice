import sys
sys.setrecursionlimit(10 ** 7)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

plan = list(map(int, sys.stdin.readline().rstrip().split()))

parent = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

parent = [-1] + parent

for i in range(1, m):
    if parent[plan[0]] != parent[plan[i]]:
        print("NO")
        break
else:
    print("YES")

