import sys;
from collections import deque;
N = int(sys.stdin.readline().rstrip());
graph = [];
line = [[] for _ in range(N)];

for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()));
    graph.append(temp);
    for j in range(N):
        if temp[j] == 1:
            line[i].append(j);

def bfs(i, j):
    queue = deque();
    visit = [False for _ in range(N)];
    arrivePoint = j;
    queue.append(i);
    while queue:
        x = queue.popleft();

        for point in line[x]:
            if point == arrivePoint:
                return True;

            if not visit[point]:
                visit[point] = True;
                queue.append(point);

    return False;

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 or bfs(i, j):
            print(1, end=" ");
        else:
            print(0, end=" ");
    print();