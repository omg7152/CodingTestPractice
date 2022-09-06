cabinet = {1 : "안세웅", 2 : "양시원"}

#출력1
# Key 값이 없으면 에러
print(cabinet[1])
print(cabinet[2])
print(cabinet[3])

# 출력2
# Key 값이 없으면 None 리턴
print(cabinet.get(1))
print(cabinet.get(2))
print(cabinet.get(3))
print(cabinet.get(3, "Key 가 없습니다.")) # Key 값이 없을 경우 디폴트 값 지정 가능

print(3 in cabinet) # Key 값이 Dictionary 안에 있는지 확인

cabinet[3] = "이찬형" # Dictionary 값 추가, 수정
cabinet[2] = "정찬호"
print(cabinet)

del cabinet[3] # Dictionary 값 삭제
print(cabinet)

print(cabinet.keys()) # Dictionary Key값 출력
print(cabinet.values()) # Dictionary Value 값 출력
print(cabinet.items()) # Dictionary Key, Value 쌍 출력

cabinet.clear() # Dictionary 초기화
print(cabinet)