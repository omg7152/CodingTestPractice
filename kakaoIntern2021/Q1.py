def solution(s):
    answer = 0
    list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        s = s.replace(list[i], str(i))
    answer = int(s)
    return answer

print(solution("23four5six7"))