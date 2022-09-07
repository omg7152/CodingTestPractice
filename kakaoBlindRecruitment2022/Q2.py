def solution(n, k):
    answer = 0

    # 진수 변환
    rev = ''
    while n > 0:
        # k로 나눈 몫을 n, 나머지를 mod 에 저장
        n, mod = divmod(n, k)
        rev += str(mod)

    # 현재 역순으로 저장 되어있어서 변경
    rev = rev[::-1]

    num_list = rev.split('0')

    for num in num_list:
        if num == '' or num == '1':
            continue
        
        # 소수 체크
        check = True
        for i in range(2, int(int(num) ** 0.5) + 1):
            if int(num) % i == 0:
                check = False
                break
        if check:
            answer += 1

    return answer

print(solution(437674, 3))
print(solution(110011, 10))