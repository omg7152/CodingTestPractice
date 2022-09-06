import sys;

N = int(sys.stdin.readline());
graph = [];
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())));

count = 0;
totalgroup = 0;

def bfs(x, y):
    global count;
    if x < 0 or x >= N or y < 0 or y >= N:
        return False;

    if graph[x][y] == 1:
        graph[x][y] = 0;
        count += 1;
        bfs(x + 1, y);
        bfs(x - 1, y);
        bfs(x, y + 1);
        bfs(x, y - 1);
        return True;
    return False;

houselist = [];
for i in range(N):
    for j in range(N):
        if bfs(i, j) == True:
            totalgroup += 1;
            houselist.append(count);
            count = 0;

houselist.sort();
print(totalgroup);
for i in houselist:
    print(i);