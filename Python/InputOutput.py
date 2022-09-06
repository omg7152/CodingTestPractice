print("python", "java", sep = ",") # 구분자 설정 가능
print("python", "java", end = "???\n") # 마지막 문자열 설정 가능(디폴트 줄바꿈 - 변경시 줄바꿈 안됨)

# 나중에 로그찍을때 사용
import sys
print("python", "java", file = sys.stdout) # 정상출력
print("python", "java", file = sys.stderr) # 에러출력


scores = {"수학" : 90, "영어" : 60, "코딩" : 100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust : 왼쪽정렬, rjust : 오른쪽정렬


for num in range(1, 25):
    print("대기번호 : " + str(num).zfill(3)) # 설정한 문자 길이에 공백은 0으로 채움


print("{0: >10}" .format(500)) # 오른쪽정렬하고 나머지부분 공백으로 채움
print("{0: >+10}" .format(500)) # 오른쪽정렬하고 나머지 공백으로 채우나 부호 추가
print("{0: >+10}" .format(-500))
print("{0:_>10}" .format(500)) # 오른쪽정렬하고 나머지 언더바로 채움

print("{0: <10}" .format(500)) # 왼쪽정렬하고 나머지부분 공백으로 채움
print("{0: <+10}" .format(500)) # 왼쪽정렬하고 나머지 공백으로 채우나 부호 추가
print("{0: <+10}" .format(-500))
print("{0:_<10}" .format(500)) # 왼쪽정렬하고 나머지 언더바로 채움

print("{0:,}" .format(10000000000)) # 3자리마다 , 추가
print("{0:+,}" .format(10000000000)) # 3자리마다 , 추가 부호 추가
print("{0:+,}" .format(-10000000000)) # 3자리마다 , 추가 부호 추가

print("{0:^<+30,}" .format(-10000000000)) # 3자리마다 , 추가 부호 추가 오른쪽정렬 나머지 ^ 로 채움

print("{0:f}" .format(5/3)) # 소수점 표시
print("{0:.3f}" .format(5/3)) # 소수점 4자리에서 반올림