import sys;

N = int(sys.stdin.readline());
cranes = list(map(int, sys.stdin.readline().rstrip().split()));
M = int(sys.stdin.readline());
boxs = list(map(int, sys.stdin.readline().rstrip().split()));
cranes.sort(reverse=True);
boxs.sort(reverse=True);

if cranes[0] < boxs[0]:
    print(-1);
    sys.exit();
else:
    result = 0;
    while len(boxs) > 0:
        result += 1;
        for crane in cranes:
            for j in range(len(boxs)):
                if crane >= boxs[j]:
                    boxs.pop(j);
                    break;
    print(result);