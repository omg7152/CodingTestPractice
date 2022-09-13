def timeToSeconds(time):
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s

def secondsToTime(s):
    time = str(s // 3600).zfill(2) + ":" + str((s % 3600) // 60).zfill(2) + ":" + str(s % 60).zfill(2)
    return time

def solution(play_time, adv_time, logs):
    answer = ''

    playSeconds = timeToSeconds(play_time)
    advSeconds = timeToSeconds(adv_time)

    graph = [0] * (playSeconds + 1)

    # 가로합 하기 위해 범위 저장
    for log in logs:
        temp = log.split('-')
        graph[timeToSeconds(temp[0])] += 1
        graph[timeToSeconds(temp[1])] -= 1

    # 가로합
    for i in range(1, playSeconds + 1):
        graph[i] += graph[i - 1]
    # 가로합 한번 더해서 누적 시간 구함
    for i in range(1, playSeconds + 1):
        graph[i] += graph[i - 1]

    # 0 부터 총 시간 - 광고시간 까지 반복하여 누적 시간이 가장 큰 시간 구함
    max_time = 0
    for i in range(playSeconds - advSeconds + 1):
        end = i + advSeconds
        if max_time < graph[end] - graph[i]:
            max_time = graph[end] - graph[i]
            answer = secondsToTime(i + 1 if i != 0 else i)
    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))