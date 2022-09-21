def solution(nodeinfo):
    answer = [[]]
    root = [0 ,0, 0]
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        if root[1] < y:
            root = [x, y, i + 1]


    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))