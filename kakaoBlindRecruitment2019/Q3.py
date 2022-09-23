from itertools import combinations

def solution(relation):
    answer = 0

    column = len(relation[0])
    student = len(relation)

    # 컬럼 조합
    combnation = []
    # 후보키가 된 조합
    result = []

    # 컬럼 개수별로 후보키 조합 저장
    for i in range(1, column + 1):
        combnation += combinations(range(column), i)

    for comb in combnation:
        setcomb = set(comb)
        check = True
        for re in result:
            # 컬럼 조합 안에 이미 후보키가 된 조합이 들어있으면 건너뜀 (집합의 차집합 이용)
            if not re - setcomb:
                check = False
                break
        if not check:
            continue

        # 컬럼내용 + / 컬럼내용 ... 하여 집합에 추가
        temp = set()
        for j in range(student):
            strKey = ""
            for k in comb:
                strKey += relation[j][k] + '/'
            temp.add(strKey)

        # 집합의 크기가 튜플의 크기와 같으면 조합 개수 증가시키고 후보키가 된 조합에 해당 조합 추가
        if len(temp) == student:
            answer += 1
            result.append(setcomb)

    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))