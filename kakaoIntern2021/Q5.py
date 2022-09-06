import sys
sys.setrecursionlimit(10 ** 7)
cnt = 0

def dfs(num, links, node, limit):
    global cnt
    Lnode, Rnode = links[node]
    left, right = 0, 0
    # 자식노드가 -1 이 아니면 자식노드 탐색
    if Lnode != -1:
        left = dfs(num, links, Lnode, limit)

    if Rnode != -1:
        right = dfs(num, links, Rnode, limit)

    # 현재노드의 인원수와 자식노드의 인원수 합이 제한 값보다 작거나 같으면
    if num[node] + left + right <= limit:
        return num[node] + left + right

    # 현재노드의 인원수와 자식노드중 인원수가 작은값의 합이 제한값 보다 작거나 같으면
    if num[node] + min(left, right) <= limit:
        # 두 자식노드중 하나를 다른 그룹으로 나누기 때문에 그룹 카운트 + 1
        cnt += 1
        return num[node] + min(left, right)

    # 두 자식노드를 각각 다른 그룹으로 나누기 떄문에 그룹 카운트 + 1
    cnt += 2
    return num[node]

def solution(k, num, links):
    global cnt
    parent = [-1 for _ in range(len(num))]

    # 루트노드를 찾기위해 각 노드별 부모노드를 저장
    for i in range(len(links)):
        left, right = links[i]

        if left != -1:
            parent[left] = i

        if right != -1:
            parent[right] = i

    root = -1
    for i in range(len(parent)):
        if parent[i] == -1:
            root = i
            break
        
    # 이분탐색으로 그룹의 최대값을 찾음
    low = max(num)
    high = 10 ** 8

    while low < high:
        # 그룹당 제한 인원수
        mid = (low + high) // 2

        cnt = 0
        dfs(num, links, root, mid)

        #마지막 그룹도 증가
        cnt += 1

        # 제한 인원수로 그룹을 나누었을때 그룹의 수가 k 보다 작거나 같으면 high 를 제한 인원수로 변경하고 
        if cnt <= k:
            high = mid
        # 그렇지 않으면 low 를 제한 인원수 + 1 로 변경
        else:
            low = mid + 1

    return low

print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
print(solution(	1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(2, [6], [[-1, -1]]))
