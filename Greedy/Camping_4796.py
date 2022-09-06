import sys;

i = 1
result = ""
while(True):
    L, P, V = list(map(int, sys.stdin.readline().rstrip().split()))

    if L == 0 and P == 0 and V == 0:
        break
    
    #총 휴가일을 연속하는 일자로 나눈 값 X 연속하는 일자 중 사용가능한 일자
    useDay = (V // P) * L
    #위의 처리 후 남은 휴가 일자
    remainDay = V % P
    
    #남은 휴가일이 연속하는 일자 중 사용가능한 일자 보다 크거나 같으면 사용가능일자 추가
    if remainDay >= L:
        useDay += L
    #남은 휴가일이 연속하는 일자 중 사용가능한 일자보다 작으면 남은 휴가일 추가
    else:
        useDay += remainDay
    
    result += "Case " + str(i) + ": " + str(useDay) + "\n"
    i += 1

print(result)
