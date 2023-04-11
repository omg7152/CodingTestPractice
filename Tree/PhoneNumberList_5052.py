import sys

class Node():
    def __init__(self):
        self.leaf = False
        self.child = {}

class Tree():
    def __init__(self):
        self.head = Node()

    def insert(self, number):
        curr = self.head
        for ch in number:
            if ch not in curr.child:
                curr.child[ch] = Node()

            curr = curr.child[ch]

        curr.leaf = True

    def search(self, number):
        curr = self.head
        for ch in number:
            if curr.leaf:
                return False
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

    
    