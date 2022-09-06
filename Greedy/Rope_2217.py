import sys
N = int(sys.stdin.readline().rstrip())
ropes = []

for i in range(N):
    ropes.append(int(sys.stdin.readline().rstrip()))

ropes.sort(reverse=True)

result = 0

for i in range(N):
    result = max(result, ropes[i] * (i + 1))

print(result)
