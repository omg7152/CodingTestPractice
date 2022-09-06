import sys;
sys.setrecursionlimit(10**7);
case = [];
moves = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]];
while True:
    w, h = list(map(int, sys.stdin.readline().rstrip().split()));
    if w == 0 and h == 0:
        break;
    graph = [];
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())));
    case.append(graph);

def dfs(graph, x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
        return False;

    if graph[x][y] == 1:
        graph[x][y] = 0;
        for move in moves:
            dx, dy = x + move[0], y + move[1];
            dfs(graph, dx, dy);
        return True;

    return False;

for i in range(len(case)):
    graph = case[i];
    result = 0;
    for j in range(len(graph)):
        for k in range(len(graph[0])):
            if dfs(graph, j, k) == True:
                result += 1;
    print(result);