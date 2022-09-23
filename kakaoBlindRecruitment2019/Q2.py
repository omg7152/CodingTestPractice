def solution(N, stages):
    answer = []
    
    stage = [0] * (N + 1)

    # 각 스테이지 도전중인 인원 수 저장
    for i in stages:
        stage[i - 1] += 1

    FailRate = []

    # [실패율, 스테이지 번호] 저장 - 실패율 : 현재 스테이지 도전중인 인원 / 현재 스테이지 도달한 인원(현재 스테이지부터 마지막까지 스테이지까지 인원수의 합)
    for i in range(N):
        FailRate.append([stage[i] / sum(stage[i:]) if sum(stage[i:]) > 0 else 0, i + 1])


    # 실패율이 큰 순서대로 정렬
    FailRate.sort(key=lambda x : x[0], reverse = True)

    # 순서대로 해당 스테이지 번호 출력
    for i in range(N):
        answer.append(FailRate[i][1])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))