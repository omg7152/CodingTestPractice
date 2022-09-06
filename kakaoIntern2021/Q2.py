def check(place):
    plist = []
    
    # 응시자 위치 찾기
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                plist.append([i,j])
    
    # 각 응시자들 끼리 비교
    for p1 in plist:
        for p2 in plist:

            if p1 == p2:
                continue
            
            # 응시자의 x축 거리차이
            diffx = abs(p1[0] - p2[0])
            # 응시자의 y축 거리차이
            diffy = abs(p1[1] - p2[1])

            #거리차이가 2 보다 크면 건너뜀
            if diffx + diffy > 2:
                continue
            
            #거리차이가 1이면 거리두기 X
            if diffx + diffy == 1:
                return 0

            # x축 거리차이가 2 이고 각 응시자 사이에 파티션이 없으면 거리두기 X
            if diffx == 2 and place[(p1[0] + p2[0]) // 2][p1[1]] != 'X':
                return 0
            # y축 거리차이가 2 이고 각 응시자 사이에 파티션이 없으면 거리두기 X
            if diffy == 2 and place[p1[0]][(p1[1] + p2[1]) // 2] != 'X':
                return 0

            # 각 축의 거리차이가 1 이고 양쪽에 파티션이 없으면 거리두기 X
            if diffx == 1 and diffy == 1 and (place[p1[0]][p2[1]] != 'X' or place[p2[0]][p1[1]] != 'X'):
                return 0

    return 1
            
def solution(places):
    answer = []
    
    for place in places:
        answer.append(check(place))
    
    return answer