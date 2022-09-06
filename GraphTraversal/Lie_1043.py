import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
truth = set(list(map(int, sys.stdin.readline().rstrip().split()))[1:])
party = []
for _ in range(m):
    party.append(set(list(map(int, sys.stdin.readline().rstrip().split()))[1:]))

for _ in range(m):
    for p in party:
        if p & truth:
            truth = truth.union(p)

ans = 0
for p in party:
    if p & truth:
        continue
    ans += 1

print(ans)