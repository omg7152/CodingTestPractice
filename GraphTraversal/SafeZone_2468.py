import sys;
import copy;
sys.setrecursionlimit(10**7);
N = int(sys.stdin.readline().rstrip());

graph = [];

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())));

def dfs(g, x, y, num):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False;

    if g[x][y] >= num:
        g[x][y] = 0
        dfs(g, x + 1, y, num);
        dfs(g, x - 1, y, num);
        dfs(g, x, y + 1, num);
        dfs(g, x, y - 1, num);
        return True;
    return False;

maxnum = max(map(max, graph));
result = 0;

for num in range(N, maxnum + 1):
    cnt = 0;
    g = copy.deepcopy(graph);
    for i in range(N):
        for j in range(N):
            if dfs(g, i, j, num) == True:
                cnt += 1;
    result = max(result, cnt);

print(result);
