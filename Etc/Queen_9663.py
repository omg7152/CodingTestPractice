#python3 - 시간초과
#pypy3 - 성공

import sys

n = int(sys.stdin.readline().rstrip())
queen = [0] * n
visit = [False] * n
result = 0

def ableCheck(x):
    for i in range(x):
        if abs(queen[x] - queen[i]) == abs(x - i):
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            if visit[i]:
                continue
            
            queen[x] = i
            if ableCheck(x):
                visit[i] = True
                dfs(x + 1)
                visit[i] = False

dfs(0)
print(result)