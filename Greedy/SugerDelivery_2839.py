import sys;

N = int(sys.stdin.readline().rstrip())

result = 0

while N >= 0:

    if N % 5 == 0:
        result += N // 5
        N = N % 5
        break
    
    result += 1
    N -= 3
else:
    result = -1

print(result)
