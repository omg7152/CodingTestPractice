def solution(queue1, queue2):
    answer = 0
    
    queue = queue1 + queue2
    half = sum(queue) // 2
    n = len(queue1)
    
    start = 0
    end = n

    startCount = 0
    endCount = 0
    
    temp = sum(queue1)
    while startCount < 2 * n and endCount < 2 * n:
            
        if temp == half:
            return answer
        elif temp > half:
            temp -= queue[start]
            start = start + 1 if start + 1 < n * 2 else 0
            startCount += 1
        else:
            temp += queue[end]
            end = end + 1 if end + 1 < n * 2 else 0
            endCount += 1
    
        answer += 1
        
    return -1