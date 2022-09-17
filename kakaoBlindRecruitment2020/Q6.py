from itertools import combinations

def dfs(num, temp, visit, comb, use):

    # 친구 조합 반복
    for i in range(len(comb)):
        # 이미 점검나간 친구 건너뜀
        if use[i]:
            continue
        
        # 최대 점검 가능 지점
        checknum = num + comb[i]
        # 해당 친구 점검 나간처리
        use[i] = True
        # 해당 친구로 점검 가능 취약 지점
        thisvisit = []

        # 전체 취약지점 반복
        for j in range(len(temp)):
            # 아직 점검하지 않은 지점
            if not visit[j]:
                # 현재 지점이 최대 점검 가능 지점보다 작거나 같으면 점검 처리
                if temp[j] <= checknum:
                    visit[j] = True
                    thisvisit.append(j)

                # 현재 지점이 최대 점검 가능 지점보다 크면 다음 친구로 점검하기 위해 재귀 호출
                else:
                    # 결과가 True 면 점검 가능함으로 True 리턴
                    if dfs(temp[j], temp, visit, comb, use):
                        return True
                    break
        
        # 모든 친구 점검 나간 후 남은 취약지점이 없으면 True리턴
        if visit.count(False) == 0:
            return True

        # 해당 친구로 점검 한 지점들 롤백
        for j in thisvisit:
            visit[j] = False
        use[i] = False

    # 전체 친구가 점검 다 나간 후에도 남은 취약지점이 있으면 False 리턴
    return False

def solution(n, weak, dist):
    answer = -1

    # 해당지점부터 직선으로 펴기위한 반복
    for i in range(len(weak)):
        # 해당지점부터 직선으로 편 weak 리스트
        # 현재 지점부터 마지막 지점 까지 리스트 + 처음 지점부터 현재지점 까지 +n 한 리스트
        temp = weak[i:] + [n + weak[j] for j in range(i)]

        # 점검할 친구 수 설정하기 위한 반복
        for j in range(1, len(dist) + 1):

            # 이미 저장된 정답 보다 설정한 친구 수가 많으면 반복문 종료
            if answer != -1 and answer < j:
                break
            
            # 설정한 친구수로 점검할 친구 조합 반복
            for comb in combinations(dist, j):
                if dfs(temp[0], temp, [False] * len(temp), comb, [False] * j):
                    answer = min(answer, j) if answer != -1 else j
                    break

    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(200, [0, 100], [1, 1]))
print(solution(50, [1], [6]))
print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))

