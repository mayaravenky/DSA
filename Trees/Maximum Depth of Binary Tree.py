class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def height_recursive(root):
    if root is None:
        return -1
    left_height = height_recursive(root.left)
    right_height = height_recursive(root.right)
    return max(left_height,right_height) + 1

def height_iterative(root):
    if root is None:
        return -1
    queue = []
    queue.append(root)
    height = -1
    while queue:
        len_level = len(queue)
        height += 1
        for i in range(len_level):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return height

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print("Height of the tree1 is:",height_recursive(root))
    print("Height of the tree1 using iterative is:",height_iterative(root))
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)
    print("Height of the tree2 is:",height_recursive(root))
    print("Height of the tree2 using iterative is:",height_iterative(root))