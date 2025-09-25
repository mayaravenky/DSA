class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data,end='->')
    inorder(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    inorder(root)

