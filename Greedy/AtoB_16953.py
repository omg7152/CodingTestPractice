import sys;
A, B = list(map(int, sys.stdin.readline().rstrip().split()))

count = 1
while True:
    #A가 B보다 크게되면 A를 B로 바꿀 수 없음
    if A > B:
        print(-1)
        break
    #A가 B와 같으면 연산횟수를 출력
    elif A == B:
        print(count)
        break
    
    #B가 2로 나누어 떨어지면 B를 2로 나눈 값을 B로 변경
    if B % 2 == 0:
        B = B // 2
    #B의 마지막 문자가 1 이면 마지막 문자 제거한 값을 B로 변경
    elif str(B)[-1:] == '1':
        B = int(str(B)[:-1])
    #주어진 연산을 할 수 없으면 A를 B로 바꿀 수 없음
    else:
        print(-1)
        break

    count += 1