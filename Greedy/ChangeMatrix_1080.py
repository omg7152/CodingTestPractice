import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

matrixA = []
matrixB = []

for i in range(N * 2):
    msg = list(sys.stdin.readline().rstrip())
    if i < N:
        matrixA.append(msg)
    else:
        matrixB.append(msg)

#행렬 변환 연산
def change(i, j):
    for cnt1 in range(3):
        for cnt2 in range(3):
            #0이면 1로 1이면 0으로 변환
            matrixA[i + cnt1][j + cnt2] = "1" if matrixA[i + cnt1][j + cnt2] == "0" else "0"

    return matrixA

result = 0
#행렬의 크기가 3 X 3 보다 클 경우
if N >= 3 and M >= 3:
    #변환을 할때 3 X 3 부분 행렬을 변환하기 때문에 N - 2 까지만 반복
    for i in range(N - 2):
        #변환을 할때 3 X 3 부분 행렬을 변환하기 때문에 M - 2 까지만 반복
        for j in range(M - 2):
            if matrixA[i][j] != matrixB[i][j]:
                matrixA = change(i, j)
                result += 1

if matrixA == matrixB:
    print(result)
else:
    print(-1)