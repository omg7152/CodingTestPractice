
def dfs(info, visited, apeach, lion, idx, remain):

    for i in range(idx, 11):

        next_apeach = apeach
        next_lion = lion
        next_remain = remain

        if info[i] < remain:
            next_apeach -= 10 - i
            next_lion += 10 - i
            next_remain -= 10 - 1

        dfs(info, visited, apeach - 10 + i, lion + 10 - i, idx + 1, remain - info[i])

def solution(n, info):
    answer = [0] * 11

    apeach = 0
    for i in range(11):
        if info[i] != 0:
            apeach += 10 - i

    visited = [0] * 11

    dfs(info, visited, apeach, 0, 0, n)

    

    return answer

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
