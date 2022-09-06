import sys
N, M = list(map(int, sys.stdin.readline().rstrip().split()))

minsetprice = 1000
minoneprice = 1000

#세트로 구매했을 때 세트 수
needSet = int(N) // 6
#나머지 줄의 수
needOne = int(N) % 6

for i in range(int(M)):
    SetPrice, OnePrice = list(map(int, sys.stdin.readline().rstrip().split()))
    minsetprice = min(minsetprice, SetPrice)
    minoneprice = min(minoneprice, OnePrice)

#세트로 구매하는 가격보다 낱개로 6개 구매하는 가격이 저렴할 경우
if minsetprice >= minoneprice * 6:
    print(minoneprice * N)
else:
    #세트의 가격보다 나머지 줄의 수 만큼 낱개로 구매하는 가격이 저렴할 경우
    if minsetprice >= minoneprice * needOne:
        print((minsetprice * needSet) + (minoneprice * needOne))
    #세트로 한세트 더 구매하는 가격이 저렴할 경우
    else:
        print(minsetprice * (needSet + 1))