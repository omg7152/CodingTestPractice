import sys
import heapq

N, K = list(map(int, sys.stdin.readline().rstrip().split()))
jewel = []
for _ in range(N):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))
bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()

result = 0
#훔칠 수 있는 보석 가격
stealableJewelPrice = []
for bag in bags:
    #남은 보석이 있고 담을 수 있는 가방의 무게가 첫번째 보석의 무게보다 크면 반복
    while jewel and bag >= jewel[0][0]:
        # 훔칠 수 있는 보석의 가격을 리스트에 저장(가장 비싼 보석부터 훔치기 위해 보석가격에 - 곱해줌)
        heapq.heappush(stealableJewelPrice, - heapq.heappop(jewel)[1])

    #훔칠 수 있는 보석이 있으면
    if stealableJewelPrice:
        #가장 작은값을 뽑아서 결과값에 추가(리스트에 담을때 - 를 곱해줬기 때문에 결과값에 더해주는게 아니라 빼줌)
        result -= heapq.heappop(stealableJewelPrice)
    #남은 보석이 없으면 종료
    elif not jewel:
        break

print(result)
