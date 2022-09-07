from collections import deque

def solution(rc, operations):
    answer = []

    # 좌 우측 끝을 제외한 각 행 
    queue = deque(deque(r[1:-1]) for r in rc)
    # 왼쪽
    left = deque([l[0] for l in rc])
    # 오른쪽
    right = deque([l[-1] for l in rc])
    
    for op in operations:
        if op == "Rotate":
            # 첫번쨰 행
            q = queue.popleft()
            q.appendleft(left.popleft())
            right.appendleft(q.pop())
            queue.appendleft(q)

            # 마지막 행
            q = queue.pop()
            q.append(right.pop())
            left.append(q.popleft())
            queue.append(q)
        else:
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            
            queue.appendleft(queue.pop())

    for i in range(len(rc)):
        q = queue.popleft()
        q.appendleft(left.popleft())
        q.append(right.popleft())
        rc[i] = list(q)
                
    return rc

print(solution(	[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))