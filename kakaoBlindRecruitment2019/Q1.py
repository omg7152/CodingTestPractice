def solution(record):
    answer = []

    user = {}
    
    for re in record:
        if re.split()[0] == "Leave":
            continue
        
        commend, id, name = map(str, re.split())

        user[id] = name

    for re in record:
        if re.split()[0] == "Leave":
            commend, id = map(str, re.split())
        else:
            commend, id, name = map(str, re.split())

        if commend == "Enter":
            answer.append(user[id] + "님이 들어왔습니다.")
        elif commend == "Leave":
            answer.append(user[id] + "님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))