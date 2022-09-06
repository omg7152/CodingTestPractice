import sys;

cnt = int(sys.stdin.readline().rstrip());
change = []
coin = [25, 10, 5, 1];

for _ in range(cnt):
    money = int(sys.stdin.readline().rstrip());
    change.append(money);
    
for i in range(cnt):
    for j in range(4):
        print(change[i] // coin[j], end=" ");
        change[i] = change[i] % coin[j];
    print();

