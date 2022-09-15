def solution(n, build_frame):
    answer = {}
    #기둥, 보-L, 보-C, 보-R
    graph = [[False, False, False, False] * (n + 1) for _ in range(n + 1)]

    for x, y, a, b in build_frame:

        if b == 1:
            if [x, y, a] in answer:
                continue
            
            # 기둥
            if a == 0:
                # 바닥에 설치, 아래쪽에 기둥이 있을경우, 왼쪽에 보가 있을경우
                if y == 0 or (y > 0 and graph[y - 1][x][0]) or graph[y][x][0]:
                    answer.add([x, y, a])
                    graph[y][x][0] = True
            # 보
            else:
                # 아래쪽에 기둥이 있을경우, 오른쪽 아래에 기둥이 있을경우, 왼쪽 오른쪽에 보가 있을 경우
                if graph[y - 1][x][0] or (y > 0 and graph[y - 1][x + 1][0]) or (graph[y][x][1] and graph[y][x][3]):
                    answer.add([x, y, a])
                    graph[y][x][2] = True
                    if x > 0:
                        graph[y][x - 1][3] = True
                    elif x < n:
                        graph[y][x + 1][1] = True
        else:
            if [x, y, a] not in answer:
                continue

            # 기둥
            if a == 0:
                # 위쪽에 기둥이 있으면 건너뜀
                if graph[y + 1][x][0]:
                    continue
                    
                # 위쪽에 보가 있고 오른쪽에 기둥이 없으며 양쪽에 보가 없을경우
                if graph[y + 1][x][2] and not graph[y][x + 1][0] and (not graph[y + 1][x][1] or not graph[y + 1][x][3]):
                    continue
                
                # x가 0보다크고 왼쪽 위에 보가 있으며 왼쪽에 기둥이 없고 양쪽에 보가 없을경우
                if x > 0 and graph[y + 1][x - 1][2] and not graph[y + 1][x - 1][0] and (not graph[y + 1][x - 1][1] or not graph[y + 1][x - 1][3]):
                    continue

                answer.remove([x, y, a])
                graph[y][x][0] = False

            # 보
            else:
                pass


    return answer

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))