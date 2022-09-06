# jumin = "960131-1228473";
# print("성별 : " + jumin[7]);
# print("연 : " + jumin[0:2]); # 0번 인덱스부터 2번인덱스 전까지
# print("월 : " + jumin[2:4]); # 2번 인덱스부터 4번인덱스 전까지
# print("일 : " + jumin[4:6]); # 4번 인덱스부터 6번인덱스 전까지
# print("생년월일 : " + jumin[:6]); # 콜론앞에 수가 없으면 처음부터
# print("뒤 7자리 : " + jumin[7:]); # 7번 인덱스부터 끝까지
# print("뒤 7자리 (뒤에서부터): " + jumin[-7:]); # 맨뒤에서 -7번째 부터 끝까지

# python = "Python Is Amazing"; 
# print(python.lower()); # 전부 소문자로 변환
# print(python.upper()); # 전부 대문자로 변환
# print(python[0].isupper()); #0번 인덱스의 값이 대문자인가
# print(len(python)); # 문자열의 길이
# print(python.replace("Python", "Java")); # 특정문자열 지정한문자열로 변환

# index = python.index("n"); # 문자열중 n의 인덱스 (첫번째 값)
# print(index);
# index2 = python.index("n", index + 1); # 문자열중 n의 인덱스 (두번째 값)
# print(index2);
# index3 = python.find("x"); # index 함수와 같지만 지정한값이 없으면 index 함수는 오류 발생하고 find 함수는 -1 리턴
# print(index3);

# print(python.count("n")); # 문자열중 지정한 값의 개수

# print("나는 %d 살 입니다." % 27); # 정수
# print("나는 %s 를 좋아해요." % "파이썬"); # 문자열
# print("Apple 이라는 단어는 %c 로 시작해요." % "A"); # 문자
# print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란")); # 여러개

# print("나는 {} 살 입니다." .format(20));
# print("나는 {}색과 {}색을 좋아해요." .format("빨간", "파란"));
# print("나는 {1}색과 {0}색을 좋아해요." .format("빨간", "파란"));
# print("나는 {age}살이고, {color}색을 좋아해요." .format(age = 27, color = "빨간"));
# age = 27;
# color = "빨간";
# print(f"나는 {age}살이고, {color}색을 좋아해요.");