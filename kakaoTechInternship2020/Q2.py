import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    operators = list(re.sub('[0-9]', '', expression))

    oplist = list(set(operators))
    ranks = permutations(oplist, len(oplist))

    for rank in ranks:
        s = expression
        rule = '0-9)('
        for r in rank:
            rule += r if r != '-' else '\-'
            part = list(map(str, re.split('[^' + rule + ']', s)))
            op = re.findall('[^' + rule + ']', s)
            s = ""
            for i in range(len(part) - 1):
                s += "(" + part[i] + ")" + op[i]

            s += "(" + part[-1] + ")"
        
        answer = max(answer, abs(eval(s)))

    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))