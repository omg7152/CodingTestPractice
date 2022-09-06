import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().rstrip().split()))



x1 = min(num)
x2 = 101
x3 = 151
result = 0
if N == 1:
    num.sort()
    result = sum(num[:5])
else:
    # 두면 최소합
    for i in range(6):
            for j in range(6):
                if i != j and j != 5 - i and x2 > num[i] + num[j]:
                    x2 = num[i] + num[j]

    # 세면 최소합
    for i in range(6):
            for j in range(6):
                if i != j and j != 5 - i:
                    for k in range(6):
                        if i != k and j != k and k != 5 - i and k != 5 - j and x3 > num[i] + num[j] + num[k]:
                            x3 = num[i] + num[j] + num[k]


    result += 4 * x3 # 세면이 보이는 값의 합
    result += ((8 * N) - 12) * x2 # 두면이 보이는 값의 합
    result += (((N-2) * (N - 2)) + (4 * (N - 2) * (N - 1))) * x1 # 한면이 보이는 값의 합

print(result)