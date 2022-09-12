from collections import deque

def solution(n, info):
    answer = []
    diff = 0

    queue = deque()
    queue.append((0, [0,0,0,0,0,0,0,0,0,0,0]))

    while queue:
        idx, arr = queue.popleft()

        # 화살을 전부 쐈을경우
        if sum(arr) == n:
            # 어피치와 라이언 점수 체크
            apeach, lion = 0, 0
            for i in range(11):
                if info[i] == arr[i] == 0:
                    continue
                if info[i] >= arr[i]:
                    apeach += 10 - i
                else:
                    lion += 10 - i

            # 라이언의 점수가 어피치 보다 크면
            if apeach < lion:
                curr_diff = lion - apeach
                # 점수차가 이전보다 작을경우
                if diff > curr_diff:
                    continue
                # 점수차가 이전보다 클경우
                if diff < curr_diff:
                    # 점수차 변경
                    diff = curr_diff
                    # 결과 리스트 초기화
                    answer.clear()
                # 결과 리스트에 추가
                answer.append(arr)
        # 화살을 제한 개수보다 많이 쐈을경우
        elif sum(arr) > n:
            continue

        # 현재 인덱스가 0점인 과녁일경우
        elif idx == 10:
            temp = arr.copy()
            # 남은 화살 개수 만큼 0점에 쏘기
            temp[idx] = n - sum(arr)
            queue.append((-1, temp))
        else:
            # 어피치보다 해당 과녁을 더많이 맞춤
            temp = arr.copy()
            temp[idx] = info[idx] + 1
            queue.append((idx + 1, temp))

            # 해당과녁 맞추지 않음
            temp2 = arr.copy()
            temp2[idx] = 0
            queue.append((idx + 1, temp2))

    return answer[-1] if answer else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
