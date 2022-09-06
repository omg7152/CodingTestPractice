import sys
T = int(sys.stdin.readline().rstrip())

count = [0, 0, 0]
button = [300, 60, 10]

for i in range(3):
    count[i] = T // button[i]
    T = T % button[i]

if T != 0:
    print(-1)
else:
    print(count[0], count[1], count[2])
