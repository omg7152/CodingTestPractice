import sys
import math

N = int(sys.stdin.readline().rstrip())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

gcd = 0
for i in range(N):
    if i == 1:
        gcd = abs(numbers[1] - numbers[0])
    gcd = math.gcd(abs(numbers[i] - numbers[i - 1]), gcd)

result = []
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)
result.append(gcd)

result = list(set(result))
result.sort()

for i in result:
    print(i, end=" ")


# 주어진 숫자 N이 오름차순이라고 가정하고, 나눠지는 숫자는 M, 나머지를 R이라고 했을때

# N[0] = K[0] * M + R

# N[1] = K[1] * M + R

# N[2] = K[2] * M + R

# 나머지 R을 없애기 위해서는

# N[i]에서 N[i - 1]을 빼주면 되는데 N[1]에서 N[0]을 빼주면

# N[1] - N[0] = M * (K[1] - K[0])

# 위처럼 될 수 있다.

# K[1] - K[0]은 N[1] - N[0]의 약수임을 알 수 있다.

#---------------------------------------------------------------------------------
# 주어진 숫자 N이 6, 34, 38이라고 했을때

# 34 - 6 = 28

# 28의 약수를 구하면 2, 4, 7, 14, 28이 될 수 있다.

# 38 - 4 = 4
 
# 4의 약수를 구하면 2, 4가 될 수 있다.

# 공통된 약수를 구하면 2, 4가 된다.

# 이는 28과 4의 최대공약수의 약수임을 알 수 있다.

#---------------------------------------------------------------------------------
# 마지막으로 약수를 구할때

# 최대공약수만큼 for문을 돌리면 시간초과가 나기때문에

# 최대공약수의 제곱근까지만 for문을 돌려주고 나머지는 계산으로 구해준다.