import sys;

N = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().rstrip().split()))
people.sort()

result = 0

#앞에 사람이 인출하는데까지 걸린 시간
temp = 0
for i in people:
    result += temp + i
    temp += i

print(result)