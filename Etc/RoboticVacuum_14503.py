import sys
sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
graph = []
moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]
result = 0

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def dfs(r, c, d, cnt):
    global result
    #현재 칸이 청소되어있지 않을 경우 청소
    if graph[r][c] == 0:
        graph[r][c] = 2
        result += 1

    #현재 뱅향의 왼쪽 칸 좌표
    nr, nc = r + moves[d][0], c + moves[d][1]

    #왼쪽 칸이 청소가 안되어있을 경우 해당칸으로 이동
    if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
        dd = d - 1 if d - 1 >= 0 else 3
        dfs(nr, nc, dd, 0)
    else:
        dd = d - 1 if d - 1 >= 0 else 3

        if cnt == 4:
            nr, nc = r + moves[dd][0], c + moves[dd][1]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != 1:
                dfs(nr, nc, d, 0)
        else:
            dfs(r, c, dd, cnt + 1)
        

dfs(r, c, d, 0)
print(result)

    


