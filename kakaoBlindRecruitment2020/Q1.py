def solution(s):
    answer = len(s)

    for i in range(1, len(s) + 1):
        # 시작 인덱스, 변경된 문자열, 반복 횟수, 반복 문자
        start, change, count, sub = i, '', 1, s[0 : i]
        while start <= len(s):
            # 시작 인덱스부터 i 개의 문자가 반복 문자와 다르거나 시작지점이 마지막일경우
            if sub != s[start : start + i] or start == len(s):
                # 반복횟수가 1이 아니면 반복 횟수 + 반복문자 를 변경된 문자열에 추가
                if count != 1:
                    change += str(count) + sub
                # 반복 횟수가 1이면 반복문자만 변경된 문자열에 추가
                else:
                    change += sub
                # 반복횟수와 다음 체크할 문자 수정
                count = 1
                sub = s[start : start + i]
            # 반복문자와 시작 인덱스부터 i 개의 문자가 같으면 반복횟수 1 증가
            else:
                count += 1
            # 시작 인덱스 i 만큼 증가
            start += i
        # 체크 후 남은 문자 변경된 문자열에 추가 (마지막에 시작 인덱스를 i 만큼 더 늘려주었기 때문에 i 만큼 뺴고 체크)
        change += s[start - i:]
        # 변경된 문자열 길이가 최소인 값 저장
        answer = min(answer, len(change))

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))