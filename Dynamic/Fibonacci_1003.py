import sys;

T = int(sys.stdin.readline().rstrip());
N = [];
#각 정수 별 1과 2를 호출하는 횟수를 저장하는 리스트
dp = [[0, 0]] * 41;

for i in range(T):
    N.append(int(sys.stdin.readline().rstrip()));

#정수가 0과 1일떄 초기값 설정
dp[0] = [1, 0];
dp[1] = [0, 1];

#각 정수별 호출횟수 저장
for i in range(2, 41):
    zeroCnt = dp[i - 2][0] + dp[i - 1][0];
    oneCnt = dp[i - 2][1] + dp[i - 1][1]
    dp[i] = [zeroCnt, oneCnt];

for n in N:
    print(dp[n][0], end=" ");
    print(dp[n][1], end=" ");
    print();
