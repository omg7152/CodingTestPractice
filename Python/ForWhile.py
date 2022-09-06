# For
for waitingNum in [1, 2, 3, 4, 5]:
    print("대기번호 : " + str(waitingNum))

for waitingNum in range(1, 6):
    print("대기번호 : " + str(waitingNum))

templist = [1, 2, 3, 4, 5]
templist = [i + 100 for i in templist] # templist For문 돌면서 i의 값에 100 을 더하여 리스트를 만들어라
print(templist)

# While
num = 1
while (num < 6):
    print("주문번호 : " + str(num))
    num += 1

num = 1
while (True):
    if num > 5:
        break
    print("주문번호 : " + str(num))
    num += 1