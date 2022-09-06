#큐 : 먼저 들어 온 데이터가 나중에 나가는 형삭(선입선출)의 자료구조
from collections import deque
queue = deque()
queue.append(1) #삽입
queue.append(2) #삽입
queue.popleft() #삭제
queue.append(3) #삽입

print(queue) #출력
queue.reverse()#역순으로 변경
print(queue) #출력