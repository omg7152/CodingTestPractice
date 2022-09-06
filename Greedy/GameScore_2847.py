import sys;

cnt = int(sys.stdin.readline().rstrip());
score = [];
for _ in range(cnt):
    score.append(int(sys.stdin.readline().rstrip()));

result = 0;
for i in reversed(range(cnt - 1)):
    if score[i + 1] <= score[i]:
        temp = score[i] - score[i + 1] + 1;
        result += temp;
        score[i] -= temp;

print(result);
