class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# 트리 초기화
root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.right.right = Node(50)

# 선주문 조회
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


# 순서 내 조회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

# 주문 후 순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
