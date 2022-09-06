def solution(n, k, cmd):
    #각 표의 연결 정보를 저장할 리스트
    linkedList = {i : [i - 1, i + 1] for i in range(n)}
    result = ['O' for _ in range(n)]
    remove = []

    for c in cmd:
        if c[0] == 'U':
            # 현재노드 변경
            for _ in range(int(c[2:])):
                k = linkedList[k][0]

        elif c[0] == 'D':
            # 현재노드 변경
            for _ in range(int(c[2:])):
                k = linkedList[k][1]

        elif c[0] == 'C':
            # 현재노드의 이전노드와 다음노드 
            before, next = linkedList[k]
            # 삭제 리스트에 현재노드 정보 저장
            remove.append([k, before, next])
            result[k] = 'X'
            
            # 다음 노드가 마지막이면 현재 위치를 이전노드, 그렇지 않으면 다음 노드로 수정
            k = before if next == n else next
            
            # 이전노드가 마지막이 아니면
            if before != -1:
                # 이전노드의 다음노드를 현재노드의 다음노드로 변경
                linkedList[before][1] = next

            # 다음노드가 마지막이 아니면
            if next != n:
                # 다음노드의 이전노드를 현재노드의 이전노드로 변경
                linkedList[next][0] = before

        elif c[0] == 'Z':
            # 가장 최근 삭제된 노드 정보
            curr, before, next = remove.pop()
            result[curr] = 'O'

            # 복구하려는 노드의 이전노드가 마지막이 아니면
            if before != -1:
                # 이전노드의 다음노드를 복구하려는 노드로 변경
                linkedList[before][1] = curr
            
            # 복구하려는 노드의 다음노드가 마지막이 아니면
            if next != n:
                # 다음노드의 이전노드를 복구하려는 노드로 변경
                linkedList[next][0] = curr

    return ''.join(result)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
