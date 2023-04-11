import sys
sys.setrecursionlimit(10 ** 7)

nums = []
lines = sys.stdin.readlines()
for line in lines:
    nums.append(int(line))

def printTree(first, end):
    if first > end:
        return

    mid = end + 1
    for i in range(first + 1, end + 1):
        if nums[first] < nums[i]:
            mid = i
            break
    printTree(first + 1, mid - 1)
    printTree(mid, end)
    print(nums[first])

printTree(0, len(nums) - 1)