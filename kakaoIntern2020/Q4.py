import heapq

def solution(board):
    n, m = len(board), len(board[0])
    cost = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = []
    heapq.heappush(queue, [0, 0, 0, -1])
    cost[0][0] = [0, 0, 0, 0]

    while queue:
        c, x, y, d= heapq.heappop(queue)

        if d != -1 and cost[x][y][d] < c:
            continue
        
        for i in range(4):
            dx, dy = x + moves[i][0], y + moves[i][1]
            dc = c + 100 if d == -1 or d == i else c + 600

            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] != 1 and cost[dx][dy][i] > dc:
                cost[dx][dy][i] = dc
                heapq.heappush(queue, [dc, dx, dy, i])

    return min(cost[n - 1][m - 1])
