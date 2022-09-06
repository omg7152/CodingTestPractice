import sys;

pay = int(sys.stdin.readline().rstrip())

coin = [500, 100, 50, 10, 5, 1]

change = 1000 - pay

result = 0
for i in coin:
    if change == 0:
        break
    else:
        result += change // i
        change = change % i

print(result)