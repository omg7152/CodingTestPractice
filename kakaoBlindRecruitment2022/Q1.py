def solution(id_list, report, k):
    answer = {}

    report_check = {}
    for id in id_list:
        report_check[id] = set([])
        answer[id] = 0

    for re in report:
        a, b = map(str, re.split())
        report_check[b].add(a)

    for a in report_check:
        if len(report_check[a]) >= k:
            for b in report_check[a]:
                answer[b] += 1


    return [answer[a] for a in answer]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))