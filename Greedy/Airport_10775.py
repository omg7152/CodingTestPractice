import sys
G = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

planes = [int(sys.stdin.readline().rstrip()) for _ in range(P)]
parent = [i for i in range(G + 1)]
result = 0


# union - find 
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    parent[y] = x

for plane in planes:
    gate = find(plane) # 내가 도킹하려는 게이트

    if gate == 0: # 도킹할수있는 게이트가 0 이면 끝
        break
    
    result += 1
    # 그 숫자부터 하나씩 도킹
    #   숫자 : 2 -> 2번게이트에 도킹,
    #   숫자 : 2 -> 1번게이트에 도킹,
    #   숫자 3 -> 3번게이트에 도킹
    #   숫자 3 -> 1, 2, 3 번게이트가 다 차서 gate == 0 임으로 반복문 끝
    union(gate - 1, gate) 

print(result)

