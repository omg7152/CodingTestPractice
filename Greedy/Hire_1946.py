import sys

T = int(sys.stdin.readline().rstrip())
case = []
result = ""
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    #지원자 리스트
    applicants = []
    for j in range(N):
        applicants.append(list(map(int, sys.stdin.readline().rstrip().split())))

    #서류결과 순으로 오름차순 정렬
    applicants.sort(key=lambda x : x[0])

    #가장 최근 합격자의 면접 성적
    passScore = applicants[0][1]
    passCount = 0
    for score in applicants:
        #면접 성적이 이전 통과자의 면접 성적보다 높을경우
        if passScore >= score[1]:
            passCount += 1
            passScore = score[1]
    result += str(passCount) + "\n"

print(result)