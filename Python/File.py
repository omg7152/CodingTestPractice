# # 파일 입출력

# score_file = open("score.txt", "w", encoding = "utf8"); # 파일오픈(쓰기전용)
# print("수학 : 0", file = score_file); # 파일에 쓰기
# print("영어 : 60", file = score_file);
# score_file.close(); # 파일 닫음

# score_file = open("score.txt", "a", encoding="utf8"); # 파일오픈(뒤에 이어서 쓰기)
# score_file.write("과학 : 90\n");
# score_file.write("코딩 : 100\n");
# score_file.close();

# score_file = open("score.txt", "r", encoding="utf8"); # 파일오픈(읽기전용)
# print(score_file.read());

# score_file = open("score.txt", "r", encoding="utf8"); # 파일오픈(읽기전용)
# print(score_file.readline()); # 한줄만 읽음
# print(score_file.readline()); # 한줄만 읽음
# print(score_file.readline()); # 한줄만 읽음
# print(score_file.readline()); # 한줄만 읽음
# score_file.close();

# score_file = open("score.txt", "r", encoding="utf8"); # 파일오픈(읽기전용)
# while(True):
#     line = score_file.readline();
#     if not line:
#         break;
#     print(line);
# score_file.close();

# score_file = open("score.txt", "r", encoding="utf8"); # 파일오픈(읽기전용)
# lines = score_file.readlines();
# for line in lines:
#     print(line);
# score_file.close();
