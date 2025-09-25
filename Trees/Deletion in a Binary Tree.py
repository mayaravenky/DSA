class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def bfs(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.data,end='->')
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

def delete_deepest(root,d_node):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        current = queue.pop(0)
        if current is d_node:
            current = None
            return
        if current.right:
            if current.right is d_node:
                current.right = None
                return
            else:
                queue.append(current.right)
        if current.left:
            if current.left is d_node:
                current.left = None
                return
            else:
                queue.append(current.left)

def deletion(root,key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    key_node = None
    queue = []
    queue.append(root)
    while len(queue) > 0:
        current = queue.pop(0)
        if current.data == key:
            key_node = current
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    if key_node:
        x = current.data
        delete_deepest(root,current)
        key_node.data = x
    return root

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data,end='->')
    inorder(node.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("Inorder traversal before deletion:",end=' ')
    inorder(root)
    key = 19
    root = deletion(root,key)
    print("\nInorder traversal after deletion:",end=' ')
    inorder(root)
    print()
    