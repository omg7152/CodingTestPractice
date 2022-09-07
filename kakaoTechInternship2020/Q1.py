def solution(numbers, hand):
    answer = ''

    left = [3, 0]
    right = [3, 2]

    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            left = [(n - 1) // 3, (n - 1) % 3]
        elif n in [3, 6, 9]:
            answer += "R"
            right = [(n - 1) // 3, (n - 1) % 3]

        else:
            x, y = 0, 0
            if n == 0:
                x, y = 3, 1
            else:
                x, y = (n - 1) // 3, (n - 1) % 3

            dl = abs(left[0] - x) + abs(left[1] - y)
            dr = abs(right[0] - x) + abs(right[1] - y)

            if dl > dr or (dl == dr and hand == "right"):
                answer += "R"
                right = [x, y]
            elif dl < dr or (dl == dr and hand == "left"):
                answer += "L"
                left = [x, y]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
