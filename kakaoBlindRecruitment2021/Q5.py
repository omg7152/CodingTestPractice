def timeToSeconds(time):
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s

def secondsToTime(s):
    time = str(s // 3600) + ":" + str((s % 3600) // 60) + ":" + str(s % 60)
    return time

def solution(play_time, adv_time, logs):
    answer = ''

    start = []
    end = []
    result = [0, '']

    for log in logs:
        temp = log.split('-')
        start.append(timeToSeconds(temp[0]))
        end.append(timeToSeconds(temp[1]))

    playSeconds = timeToSeconds(play_time)
    advSeconds = timeToSeconds(adv_time)

    if playSeconds == advSeconds:
        return "00:00:00"

    for seconds in start:
        pass

    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))