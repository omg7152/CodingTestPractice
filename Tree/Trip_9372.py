import sys

t = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())

    answer.append(n - 1)

print(*answer, sep='\n')

    