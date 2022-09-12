from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    answer = []

    # 주문 조합 개수
    for count in course:
        # 각 조합별 주문 횟수 저장 dict
        comb = defaultdict(int)
        # 주문내역
        for order in orders:
            # 주문 내역을 조합 개수로 조합하여 카운트 증가
            for menus in combinations(list(order), count):
                temp = list(menus)
                temp.sort()
                comb[''.join(temp)] += 1
        # 가장 큰 값을 배열에 추가
        [answer.append(k) for k, v in comb.items() if max(comb.values()) == v and v > 1]
    # 오름차순으로 정렬
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))