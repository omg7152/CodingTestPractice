def solution(record):
    answer = []

    user = {}
    
    # 채팅방에 들어왔거나 닉네임을 변경했을 때 현재 닉네임을 dict에 id 를 키로하여 저장
    for re in record:
        if re.split()[0] == "Leave":
            continue
        commend, id, name = map(str, re.split())
        user[id] = name

    # record를 반복하면서 각각 id값으로 현재 닉네임으로 하여 메세지 출력
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