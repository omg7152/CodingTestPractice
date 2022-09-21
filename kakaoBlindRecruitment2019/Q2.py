def solution(N, stages):
    answer = []
    
    stage = [0] * (N + 1)

    for i in stages:
        stage[i - 1] += 1

    temp = []

    for i in range(N):
        temp.append([stage[i] / sum(stage[i:]) if sum(stage[i:]) > 0 else 0, i + 1])


    temp.sort(key=lambda x : x[0], reverse = True)
    for i in range(N):
        answer.append(temp[i][1])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))