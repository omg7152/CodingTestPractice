# trie 구조
# 문자열의 집합을 표현하는 트리구조
# 두 문자열을 비교하기 위해 문자열의 길이만큼 시간이 걸리게 된다 O(MlogN)
# 이 단점을 해결하기 위해 특화된 자료구조
# 문자열의 접두사들에 대응되는 노드들이 서로 연결된 트리이다
# 한 문자열에서 현재문자의 다음 문자가 현재문자의 자식노드가 된다
# 백준 5052번

import sys

# 노드
class Node():
    def __init__(self):
        # 리프노드 여부
        self.leaf = False
        # 자식노드
        self.child = {}

class Tree():
    def __init__(self):
        # 루트노드
        self.head = Node()

    def insert(self, number):
        curr = self.head
        for ch in number:
            # 현재노드의 자식노드 중 해당 문자가 없으면 추가
            if ch not in curr.child:
                curr.child[ch] = Node()

            # 현재노드를 해당문자의 노드로 변경
            curr = curr.child[ch]
        
        # 문자열 반복 후 리프노드여부를 True로 변경
        curr.leaf = True

    def search(self, number):
        curr = self.head
        for ch in number:
            # 전체 문자를 반복하면서 해당 문자가 리프노드 라면 False 리턴
            if curr.leaf:
                return False

            # 다음 노드
            curr = curr.child[ch]

        return True
            
t = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    numbers = []

    for _ in range(n):
        numbers.append(sys.stdin.readline().rstrip())

    tree = Tree()

    for number in numbers:
        tree.insert(number)

    ans = True
    for number in numbers:
        if not tree.search(number):
            ans = False
            break

    answer.append('YES' if ans else 'NO')

print(*answer, sep='\n')