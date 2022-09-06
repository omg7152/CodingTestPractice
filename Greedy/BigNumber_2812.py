import sys

N, K = list(map(int, sys.stdin.readline().rstrip().split()))

msg = sys.stdin.readline().rstrip()
num = [msg[i] for i in range(len(msg))]

k, stack = K, []

for i in range(N):
    while(k > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        k -= 1
    stack.append(num[i])

print(''.join(stack[:N - K]))
