import sys

T = int(sys.stdin.readline())
cases = []
for i in range(T):
    N = int(sys.stdin.readline())
    cases.append(list(map(int, sys.stdin.readline().rstrip().split())))

for case in cases:
    case.sort()
    lv = 0
    if len(case) % 2 == 0:
        for i in range(len(case) - 2):
            if case[i + 2] - case[i] > lv:
                lv = case[i + 2] - case[i]
    else:
        for i in range(len(case) - 3):
            if case[i + 2] - case[i] > lv:
                lv = case[i + 2] - case[i]
        if case[-1] - case[-2] > lv:
            lv = case[-1] - case[-2]
        if case[-1] - case[-3] > lv:
            lv = case[-1] - case[-3]
    print(str(lv))
        