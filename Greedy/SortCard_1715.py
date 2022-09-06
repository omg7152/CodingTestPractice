import sys;
import heapq;
N = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(N):
        heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

if len(cards) == 1:
    print(0)
else:
    result = 0
    while True:
        A = heapq.heappop(cards)
        B = heapq.heappop(cards)
        result += A + B
        
        if not cards:
            break
            
        heapq.heappush(cards, A + B)

    print(result)