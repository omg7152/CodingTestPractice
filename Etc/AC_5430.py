import re
import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    p = deque(list(sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline().rstrip())
    numbers = deque(re.sub('[\[\]]', '', sys.stdin.readline().rstrip()).split(','))

    rev = 0
    error = False
    while p:
        fn = p.popleft()

        if fn == 'R':
            rev = 1 if rev == 0 else 0
        else:
            if numbers and n != 0:
                if rev == 0:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                error = True
                break

    if error:
        print("error")
    else:
        print("[", end="")
        if rev == 0:
            print(','.join(str(i) for i in numbers), end="")
        else:
            print(','.join(str(i) for i in reversed(numbers)), end="")
        print("]")