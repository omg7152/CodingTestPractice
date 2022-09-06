import sys;
T = int(sys.stdin.readline().rstrip());
case = [];

for i in range(T):
    M, N, K = list(map(int, sys.stdin.readline().rstrip().split()));
    case.append([[0 for _ in range(M)] for _ in range(N)]);
    for j in range(K):
        x, y = list(map(int, sys.stdin.readline().rstrip().split()));
        case[i][y][x] = 1;

def bfs(i, x, y):
    if x < 0 or x >= len(case[i]) or y < 0 or y >= len(case[i][0]):
        return False;
    
    if case[i][x][y] == 1:
        case[i][x][y] = 0;
        bfs(i, x - 1, y);
        bfs(i, x + 1, y);
        bfs(i, x, y - 1);
        bfs(i, x, y + 1);
        return True;
    return False;

for i in range(T):
    result = 0;
    for j in range(len(case[i])):
        for k in range(len(case[i][0])):
            if bfs(i, j, k) == True:
                result += 1;

    print(result);
