import sys
N = int(sys.stdin.readline().rstrip())

x = 1
while True:
    if N < x * (x + 1) / 2:
        break

    x += 1

print(x - 1)
