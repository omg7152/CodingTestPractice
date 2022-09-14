from collections import defaultdict
import re

def solution(words, queries):
    answer = []

    queriesDict = defaultdict(int)

    for query in queries:
        if query in queriesDict:
            continue

        n = len(query)

        if not re.search('[a-z]', query):
            for w in words:
                if n == len(w):
                    queriesDict[query]  += 1
            continue
            

        for word in words:
            check = True
            if n == len(word):
                for i in range(n):
                    if query[i] == '?':
                        continue
                    if query[i] != word[i]:
                        check = False
                        break

                if check:
                    queriesDict[query] += 1

    for q in queries:
        answer.append(queriesDict[q])

    return answer

print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))