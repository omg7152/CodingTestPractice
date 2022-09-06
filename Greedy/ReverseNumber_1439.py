import sys

number = sys.stdin.readline().rstrip()
result = 1
for i in range(len(number) - 1):
    #현재문자와 다음 문자가 다를 경우 분리 횟수 1 증가
    if number[i] != number[i + 1]:
        result += 1

print(result // 2)