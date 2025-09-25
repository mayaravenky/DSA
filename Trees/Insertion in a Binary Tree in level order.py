from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def insert(root,key):
    new_node = Node(key)
    if root is None:
        root = new_node
        return root
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node.left is None:
            node.left = new_node
            return root
        else:
            queue.append(node.left)
        if node.right is None:
            node.right = new_node
            return root
        else:
            queue.append(node.right)
    return root

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data,end=' ')
    inorder(node.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("Inorder traversal before insertion:",end=' ')
    inorder(root)
    key = 12
    root = insert(root,key)
    print("\nInorder traversal after insertion:",end=' ')
    inorder(root)
