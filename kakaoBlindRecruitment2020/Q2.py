def check(s):
    if s == '':
        return ''

    u, v = '', ''
    left, right = 0, 0

    for i in range(len(s)):

        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            u += s[i]
            v = s[i + 1:]
            break
        else:
            u += s[i]

    left, right = 0, 0
    currect = True
    for i in range(len(u)):
        if u[i] == '(':
            left += 1
        else:
            right += 1

        if right > left:
            currect = False
            break

    if currect:
        return u + check(v)
    else:
        changeV = '(' + check(v) + ')'

        changeU = ''

        for i in range(1, len(u) - 1):
            if u[i] == '(':
                changeU += ')'
            else:
                changeU += '('

        return changeV + changeU

def solution(p):
    answer = check(p)

    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
