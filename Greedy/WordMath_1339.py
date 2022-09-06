import sys
N = int(sys.stdin.readline().rstrip())

#알파벳의 개수가 26개이기 때문에 크기가 26인 리스트 생성
alphabet = [0 for i in range(26)]
words = []

for i in range(N):
    words.append(sys.stdin.readline().strip())

for word in words:
    lenword = len(word)
    for i in range(lenword):
        #각 문자의 아스키코드값 - 65(A가 0번 인덱스가 되기 위해 A의 아스키코드 값을 빼줌)를 하여 
        #해당 인덱스에 현재문자의 자리수만큼 10의 거듭제곱을 더해줌(ABC 일경우 A에 100, B에 10, C에 1)
        alphabet[ord(word[i]) - 65] += 10 ** (lenword - 1 - i)

#최대값을 구하기위해 내림차순 정렬
alphabet.sort(reverse=True)

num = 9
result = 0
for alp in alphabet:
    if alp == 0:
        break

    result += alp * num
    num -= 1

print(result)