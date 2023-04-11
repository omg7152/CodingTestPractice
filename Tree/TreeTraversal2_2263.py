import sys

def getPreOrder(in_idx, post_idx):

    answer.append(postorder[post_idx])

    getPreOrder(0, post_idx - in_idx)



n = int(sys.stdin.readline().rstrip())

inorder = list(map(int, sys.stdin.readline().rstrip().split()))
postorder = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []

getPreOrder(inorder.index(postorder[-1]), n - 1)

print(*answer, sep=' ')

