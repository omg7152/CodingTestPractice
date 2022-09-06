#재귀함수 : 자기자신을 다시 호출하는 함수
#   재귀함수를 문제풀이에 활용 할 경우 재귀함수의 종료 조건을 반드시 명시해야 함
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서 ', i + 1, '번째 재귀함수를 호출 합니다.');
    recursive_function(i + 1);
    print(i, '번째 재귀함수를 종료 합니다.');

recursive_function(1);

#팩토리얼 : n! => 1부터 n까지의 자연수를 모두 곱한 값 (0!, 1! = 1)
def factorial(n):
    if n <= 1:
        return 1;

    return n * factorial(n - 1);

print(factorial(5));