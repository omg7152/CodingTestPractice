import re

def solution(new_id):
    answer = new_id

    # new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    answer = answer.lower()
    # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer = re.sub('[^a-z0-9-_.]', '', answer)
    # new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer = re.sub('\.{2,}', '.', answer)
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = re.sub('^\.', '', answer)
    answer = re.sub('\.$', '', answer)
    # new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    answer = 'a' if answer == '' else answer
    #new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    answer = answer[0:15] if len(answer) > 15 else answer
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    answer = re.sub('\.$', '', answer)

    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    temp = ''
    for i in range(3 - len(answer)):
        temp += answer[-1]
    answer += temp
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))