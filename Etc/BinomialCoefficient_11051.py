import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

dp = [[0] for i in range(A + 2)]

for i in range(1, A + 2):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])

for i in range(A + 2):
    print(dp[i])

print(dp[A + 1][B + 1] % 10007)

#파스칼 삼각형을 2차원 리스트로 구현

# 우선 맨 왼쪽과 맨 오른쪽의 값은 1로 고정이다.

# 나머지는 왼쪽 대각선 위의 값과 오른쪽 대각선 위의 값을 더한 값을 넣어준다.