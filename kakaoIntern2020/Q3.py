def solution(gems):

    kind = len(set(gems))
    gems = [""] + gems
    lengems = len(gems)

    answer = [1, lengems]

    start = 1
    end = 1
    dic = {gems[1] : 1}
    while start < lengems and end < lengems:

        # 현재 범위안의 보석 종류가 전체 보석 종류와 같으면
        if len(dic) == kind:
            # 현재 구매하려는 진열대의 길이가 이전에 저장 된 길이보다 작으면 변경
            if answer[1] - answer[0] + 1 > end - start + 1:
                answer = [start, end]
            # 시작지점을 1 증가시키는데 현재 범위에서 시작지점의 보석 개수가 1 이면 딕셔너리에서 삭제
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            # 그렇지 않으면 1 감소
            else:
                dic[gems[start]] -= 1
            # 시작지점 증가
            start += 1

        # 현재 범위안의 보석 종류가 전체 보석종류와 다르면
        else:
            # 끝지점 1 증가
            end += 1
            # 증가되기전 지점이 마지막이면 종료
            if end == lengems:
                break
            # 증가된 지점의 보석 딕셔너리에 추가
            dic[gems[end]] = dic.get(gems[end], 0) + 1

    return answer