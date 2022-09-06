import sys
import heapq
N = int(sys.stdin.readline().rstrip())

Pnum = [] #양수 리스트
Nnum = [] #음수 리스트

for i in range(N):
    number = int(sys.stdin.readline().rstrip())
    if number > 0:
        heapq.heappush(Pnum, number)
    else:
        heapq.heappush(Nnum, number)

result = 0
while True:
    #음수
    if Nnum:
        #남은 개수가 1개일경우
        if len(Nnum) == 1:
            #한개 꺼내어 결과값에 더해줌
            result += heapq.heappop(Nnum)

        #남은 개수가 1개가 아니면
        else:
            #두수를 꺼내어 결과값에 두수의 곱을 더해줌
            result += heapq.heappop(Nnum) * heapq.heappop(Nnum)

    #양수
    elif Pnum:
        #개수가 홀수 일 경우 
        if len(Pnum) % 2 != 0:
            #한개 꺼내서 결과값에 더해줌
            result += heapq.heappop(Pnum)

        #개수가 짝수 일 경우
        else:
            #두개 꺼냄
            A, B = heapq.heappop(Pnum), heapq.heappop(Pnum)

            #두수 중에 하나라도 1이면 결과값에 두수의 합을 더해줌
            if A == 1 or B == 1:
                result += A + B

            #그렇지 않으면 결과값에 두수의 곱을 더해줌
            else:
                result += A * B
    
    #모든수를 처리 했을때 반복문 종료
    else:
        break

print(result)