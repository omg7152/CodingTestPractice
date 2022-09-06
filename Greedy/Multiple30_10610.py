import sys

N = list(map(int, sys.stdin.readline().rstrip()))
N.sort(reverse=True)
if 0 not in N or sum(N) % 3 != 0:
    print(-1)
else:
    print(''.join(map(str, N)))