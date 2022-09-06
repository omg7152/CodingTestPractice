import sys;
R, C = list(map(int, sys.stdin.readline().rstrip().split()));
graph = [];
moves = [[1, 0],[-1, 0],[0, 1],[0, -1]];
visit = [False for _ in range(27)];

for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()));

result = 1;
def dfs(x, y, z):
    global result;
    result = max(result, z);
    for move in moves:
        dx, dy = x + move[0], y + move[1];

        if 0 <= dx < R and 0 <= dy < C and visit[ord(graph[dx][dy]) - 65] == False:
            visit[ord(graph[dx][dy]) - 65] = True;
            dfs(dx, dy, z + 1);
            visit[ord(graph[dx][dy]) - 65] = False;
    

visit[ord(graph[0][0]) - 65] = True;
dfs(0, 0, 1);
print(result);
