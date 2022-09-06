#비트마스크

check = 0b101010101010
print("기존 데이터 : " + bin(check))
#원소추가
n = 2
print("원소추가(" + str(n) + ") : " + bin(check | (1 << n)))

#원소삭제
n = 1
print("원소삭제(" + str(n) + ") : " + bin(check & ~(1 << n)))

#원소조회
n = 3
print("원소조회(" + str(n) + ") : " + bin(check & (1 << n)))

#원소토글
n = 5
check ^= (1 << n)
print("원소토글1(" + str(n) + ") : " + bin(check & (1 << n)))
check ^= (1 << n)
print("원소토글2(" + str(n) + ") : " + bin(check & (1 << n)))
check ^= (1 << n)
print("원소토글3(" + str(n) + ") : " + bin(check & (1 << n)))
check ^= (1 << n)
print("원소토글4(" + str(n) + ") : " + bin(check & (1 << n)))