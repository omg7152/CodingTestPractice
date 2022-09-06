import sys

N = int(sys.stdin.readline().rstrip())
conferences = []

for i in range(N):
    conferences.append(list(map(int, sys.stdin.readline().rstrip().split())))

#각 회의를 끝나는 시간, 시작시간을 순서대로 오름차순 정렬한다.
conferences.sort(key=lambda x : (x[1], x[0]))

#진행한 회의 리스트
room = []

for conference in conferences:
    if not room:
        room.append(conference)
        continue
    
    #이전 회의의 끝나는 시간이 현재 회의의 시작시간보다 작거나 같으면 회의 진행
    if room[-1][1] <= conference[0]:
        room.append(conference)

print(len(room))
