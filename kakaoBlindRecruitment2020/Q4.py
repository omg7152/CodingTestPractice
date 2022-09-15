# trie 구조
# 문자열의 집합을 표현하는 트리구조
# 두 문자열을 비교하기 위해 문자열의 길이만큼 시간이 걸리게 된다 O(MlogN)
# 이 단점을 해결하기 위해 특화된 자료구조
# 문자열의 접두사들에 대응되는 노드들이 서로 연결된 트리이다
# 한 문자열에서 현재문자의 다음 문자가 현재문자의 자식노드가 된다

class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
        self.count = 0

    def insert(self, word):
        # 현재노드 = 루트노드
        self.count += 1
        curr = self.head
        
        for ch in word:
            # 자식노드에 해당문자가 없으면 추가
            if ch not in curr.child:
                curr.child[ch] = Node(ch)
            # 현재노드를 자식노드의 해당문자로 변경 후 카운트 증가
            curr = curr.child[ch]
            curr.count += 1

    def search(self, query):
        curr = self.head

        for ch in query:
            # 자식노드에 해당 문자가 없으면 0 리턴
            if ch not in curr.child:
                return 0
            else:
                # 현재노드를 해당 자식노드로 변경
                curr = curr.child[ch]
        # 반복문 종료 후 해당 노드의 count 리턴
        return curr.count

def solution(words, queries):
    answer = []

    front_trie = {}
    back_trie = {}

    for word in words:
        # dict 안에 해당 길이의 trie가 없으면 추가 해줌
        if len(word) not in front_trie:
            front_trie[len(word)] = Trie()
            back_trie[len(word)] = Trie()

        # 해당 길이의 trie 에 단어 추가
        # 정방향
        front_trie[len(word)].insert(word)
        # 역방향
        back_trie[len(word)].insert(word[::-1])

    for query in queries:
        n = len(query)
        # 해당길이의 trie가 없으면 0 추가
        if n not in front_trie:
            answer.append(0)
            continue
        
        # 쿼리문자들이 전부 '?' 이면 해당 길이의 trie.count 추가
        if n == query.count('?'):
            answer.append(front_trie[n].count)
            continue

        # '?' 가 접미사에 있을경우 앞에서부터 검색
        if query[-1] == '?':
            qcnt = query.count('?')
            answer.append(front_trie[n].search(query[:-qcnt]))
        # '?' 가 접두사에 있을경우 뒤에서부터 검색
        else:
            qcnt = query.count('?')
            answer.append(back_trie[n].search(query[qcnt:][::-1]))

    return answer

print(solution(	["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))