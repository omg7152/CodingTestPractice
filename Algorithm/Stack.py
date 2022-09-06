#스택 : 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
stack = []
stack.append(1) #삽입
stack.append(2) #삽입
stack.pop() #삭제
stack.append(3) #삽입

print(stack) #출력
print(stack[::-1])#역순으로 출력