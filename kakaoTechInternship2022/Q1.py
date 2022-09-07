def solution(survey, choices):
    answer = ''
    
    check = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    arr = ["RT", "CF", "JM", "AN"]
    
    for i in range(len(survey)):
        a, b = list(survey[i])
        
        if choices[i] > 4:
            check[b] += choices[i] - 4
        elif choices[i] < 4:
            check[a] += 4 - choices[i]
            
    for t in arr:
        a, b = list(t)
        
        if check[a] >= check[b]:
            answer += a
        else:
            answer += b
        
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))