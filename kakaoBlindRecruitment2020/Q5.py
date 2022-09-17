# 설치 가능 여부 체크
def check(n, x, y, a, graph):
    # 기둥
    # 바닥, 아래에 기둥이 있을경우, 해당 위치에 보가 있을경우, 왼쪽에 보가 있을경우 설치 가능
    if a == 0 and y != n and (y == 0 or graph[x][y - 1][0] or graph[x][y][1] or (x > 0 and graph[x - 1][y][1])):
        return True

    # 보
    # 바닥이 아니고 맨 오른쪽이 아닌 좌표 중 - 아래에 기둥이 있을경우, 양 옆에 보가 있을경우, 오른쪽 아래에 기둥이 있을경우 설치 가능
    if a == 1 and y > 0 and x < n and (graph[x][y - 1][0] or (x > 0 and graph[x - 1][y][1] and graph[x + 1][y][1]) or graph[x + 1][y - 1][0]):
        return True

    return False
    
def solution(n, build_frame):
    answer = set()

    graph = [[[False, False] for _ in range(n + 1)] for _ in range(n + 1)]

    for x, y, a, b in build_frame:

        if b == 1:
            if check(n, x, y, a, graph):
                answer.add(str(x) + '/' + str(y) + '/' + str(a))
                graph[x][y][a] = True
        else:
            # 현재위치 구조물 제거
            graph[x][y][a] = False
            answer.remove(str(x) + '/' + str(y) + '/' + str(a))
            checkDelete = True
                
            # 현재 만들어진 구조물 조건 체크
            for ans in answer:
                ax, ay, aa = map(int, ans.split('/'))

                if not check(n, ax, ay, aa, graph):
                    checkDelete = False
                    break
            
            # 제거 할 수 없으면 제거한 구조물 복구
            if not checkDelete:
                graph[x][y][a] = True
                answer.add(str(x) + '/' + str(y) + '/' + str(a))

    answer = [list(map(int, a.split('/'))) for a in answer]
    answer.sort(key=lambda x : (x[0], x[1], x[2]))
    return answer

# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1], [1, 1, 0, 1]]))
print(solution(100, [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]))