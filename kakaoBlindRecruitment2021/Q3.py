from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []

    # 각 키별로 점수를 저장할 dict
    infoDict = defaultdict(list)

    for i in range(len(info)):
        infolist = list(map(str, info[i].split()))

        for a in range(5):
            # - 를 추가할 조홥
            for b in combinations([0, 1, 2, 3], a):
                temp = ''
                for c in range(4):
                    # 조합에 인덱스가 있으면 키 에 - 추가
                    if c in b:
                        temp += '-'
                    # 그렇지 않으면 해당 인덱스 info 값 추가
                    else:
                        temp += infolist[c]
                # dict 에 추가
                infoDict[temp].append(int(infolist[-1]))

    # dict 오름차순으로 정렬
    for i in infoDict:
        infoDict[i].sort()

    for q in query:
        qlist = q.replace(' and', '').split()
        key, value = ''.join(qlist[:-1]), int(qlist[-1])

        # dict 에 있으면 
        if key in infoDict:
            #이분탐색
            low, high = 0, len(infoDict[key])

            while low < high:
                mid = (low + high) // 2
                if infoDict[key][mid] >= value:
                    high = mid
                else:
                    low = mid + 1
            
            answer.append(len(infoDict[key]) - high)
        else:
            answer.append(0)
        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))