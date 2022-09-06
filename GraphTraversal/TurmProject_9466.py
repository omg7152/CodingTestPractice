import sys
sys.setrecursionlimit(10 ** 7)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    num = group[x]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

T = int(sys.stdin.readline().rstrip())

ans = []

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    group = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    ans.append(n - len(result))

print(*ans, sep='\n')