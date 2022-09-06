import sys;
N, M = list(map(int, sys.stdin.readline().strip().split()));

holeList = list(map(int, sys.stdin.readline().strip().split()));
holeList.sort();

temp = 0;
result = 0;
for hole in holeList:
    if hole > temp:
        temp = hole + M - 1;
        result += 1;

print(result);
    
