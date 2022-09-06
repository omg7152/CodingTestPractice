import sys
cnt = int(sys.stdin.readline())

weightList = [int(i) for i in sys.stdin.readline().strip().split()]
weightList.sort()

result = 1

# 해당추 전까지 추의 합이 현재 추보다 작으면 만들 수 없음
for weight in weightList:
    if weight > result:
        break
    
    result += weight

print(result)
        
