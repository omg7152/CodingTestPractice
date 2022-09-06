import sys;

R, C = list(map(int, sys.stdin.readline().rstrip().split()));

area = [sys.stdin.readline().rstrip() for _ in range(R)];
visit = [[False] * C for _ in range(R)];
moves = [[-1, 1], [0, 1], [1, 1]];
result = 0;

def check(i, j):
    if j == C - 1:
        return True;

    for move in moves:
        nx = i + move[0];
        ny = j + move[1];
        if 0 <= nx < R and 0 <= ny < C and area[nx][ny] != 'x' and not visit[nx][ny]:
            visit[i][j] = True;
            if check(nx, ny):
                return True;
    
    return False;

for i in range(R):
    if check(i, 0):
        result += 1;

print(result);