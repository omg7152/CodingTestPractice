import sys
import math
n = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

op = list(map(int, sys.stdin.readline().rstrip().split()))

strop = []

visit = [False for _ in range(sum(op))]

for i in range(4):
    for j in range(op[i]):
        if i == 0:
            strop.append(0)
        elif i == 1:
            strop.append(1)
        elif i == 2:
            strop.append(2)
        else:
            strop.append(3)


maxResult = float('-inf')
minResult = float('inf')
def dfs(idx, r):

    if idx == n:
        global maxResult, minResult
        maxResult = max(maxResult, r)
        minResult = min(minResult, r)
        return

    for i in range(len(strop)):
        if visit[i]:
            continue

        s = strop[i]
        visit[i] = True
        temp = 0
        if s == 0:
            temp = r + numbers[idx]
        elif s == 1:
            temp = r - numbers[idx]
        elif s == 2:
            temp = r * numbers[idx]
        else:
            temp = math.trunc(r / numbers[idx])
            

        dfs(idx + 1, temp)
        visit[i] = False

dfs(1, numbers[0])
print(maxResult)
print(minResult)