def solution(food_times, k):
    answer = 0

    n = len(food_times)
    temp = []

    if sum(food_times) <= k:
        return -1

    # 각 음식별로 시간, 번호 저장 후 음식 시간을 오름차순으로 정렬
    for i in range(len(food_times)):
        temp.append([food_times[i], i + 1])
    temp.sort()

    remove = 0
    idx = 0
    
    while remove < k and idx < n:
        next = temp[idx][0] * (n - idx) if idx == 0 else (temp[idx][0] - temp[idx - 1][0]) * (n - idx)
        if next + remove > k:
            break
        remove += next
        idx += 1

    temp = sorted(temp[idx:], key=lambda x : x[1])
    answer = temp[(k - remove) % len(temp)][1]


    return answer

# print(solution([3, 1, 2], 5))
# print(solution([200, 150, 160], 451))
print(solution([6, 5, 1, 4], 200))