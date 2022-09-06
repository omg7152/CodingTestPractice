import sys
n = int(sys.stdin.readline().rstrip())

s = []
visit = [False] * n
minresult = float('inf')

for i in range(n):
    s.append(list(map(int, sys.stdin.readline().rstrip().split())))

def getAbility(team):
    result = 0

    for i in range(n // 2):
        for j in range(n // 2):
            if i == j:
                continue
            
            result += s[team[i]][team[j]]

    return result

def checkdiff():
    global minresult
    start = []
    link = []

    for i in range(n):
        if visit[i]:
            start.append(i)
        else:
            link.append(i)

    minresult = min(minresult, abs(getAbility(start) - getAbility(link)))
    
def getMember(x, y):
    if x == n // 2:
        checkdiff()
        return

    for i in range(y, n):
        if visit[i]:
            continue

        visit[i] = True
        getMember(x + 1, i)
        visit[i] = False

getMember(0, 0)
print(minresult)
