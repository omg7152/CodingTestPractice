import sys
sys.setrecursionlimit(10 ** 7)

def getOrder(arrX, arrY, answer1, answer2):
    # Y값이 가장 큰 노드를 루트노드로 설정
    node = arrY[0]
    # X값으로 정렬한 리스트에서 루트노드의 인덱스 
    idx = arrX.index(node)

    # 루트노드의 보다 X값이 큰 노드 리스트
    arrY1 = []
    # 루트노드의 보다 X값이 작은 노드 리스트
    arrY2 = []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])

    # 전위 순회 리스트에 루트노드 번호 추가
    answer1.append(node[2])

    if len(arrY1) > 0:
        # 루트노드보다 X값이 큰 노드가 있으면 X값으로 정렬한 리스트 중 index가 루트노드보다 큰 값들로 탐색 함수 재호출
        getOrder(arrX[:idx], arrY1, answer1, answer2)

    if len(arrY2) > 0:
        # 루트노드보다 X값이 작은 노드가 있으면 X값으로 정렬한 리스트 중 index가 루트노드보다 작은 값들로 탐색 함수 재호출
        getOrder(arrX[idx + 1:], arrY2, answer1, answer2)

    # 후위 순회 리스트에 루트노드 번호 추가
    answer2.append(node[2])
    return

def solution(nodeinfo):
    answer = [[], []]

    # 노드번호 추가
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    # X값 기준으로 오름차순 정렬
    arrX = sorted(nodeinfo)
    # Y값 기준으로 내림차순 정렬 후 X값으로 오름차순 정렬
    arrY = sorted(nodeinfo, key=lambda x : (-x[1], x[0]))

    getOrder(arrX, arrY, answer[0], answer[1])

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))