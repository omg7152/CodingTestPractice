import sys
expressions = sys.stdin.readline().rstrip().split("-")

result = sum(map(int, expressions[0].split("+")))

for i in range(1, len(expressions)):
    result -= sum(map(int, expressions[i].split("+")))

print(result)
