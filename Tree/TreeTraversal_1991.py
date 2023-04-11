import sys

def setPreOrder(answer, tree, node):
    left, right = tree[node]
    answer.append(node)
    if left != '.':
        setPreOrder(answer, tree, left)

    if right != '.':
        setPreOrder(answer, tree, right)

def setInOrder(answer, tree, node):
    left, right = tree[node]

    if left != '.':
        setInOrder(answer, tree, left)

    answer.append(node)

    if right != '.':
        setInOrder(answer, tree, right)

def setPostOrder(answer, tree, node):
    left, right = tree[node]
    
    if left != '.':
        setPostOrder(answer, tree, left)

    if right != '.':
        setPostOrder(answer, tree, right)

    answer.append(node)

n = int(sys.stdin.readline().rstrip())

tree = {}

for i in range(n):
    node, left, right = map(str, sys.stdin.readline().rstrip().split())

    tree[node] = [left, right]

preorder = []
inorder = []
postorder = []

setPreOrder(preorder, tree, 'A')
setInOrder(inorder, tree, 'A')
setPostOrder(postorder, tree, 'A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))

