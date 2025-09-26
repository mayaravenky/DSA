class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def min_depth_recursive(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if not root.left:
        return min_depth_recursive(root.right) + 1
    if not root.right:
        return min_depth_recursive(root.left) + 1       
    return min(min_depth_recursive(root.left),min_depth_recursive(root.right)) + 1  


def min_depth_iterative(root):
    if root is None:
        return 0
    queue = []
    queue.append((root,1))
    while queue:
        node,depth = queue.pop(0)
        if node.left is None and node.right is None:
            return depth
        if node.left:
            queue.append((node.left,depth+1))
        if node.right:
            queue.append((node.right,depth+1))
    return 0

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print("Minimum Depth of the tree using recursive is:",min_depth_recursive(root))
    print("Minimum Depth of the tree using iterative is:",min_depth_iterative(root))
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)
    print("Minimum Depth of the tree2 using recursive is:",min_depth_recursive(root))
    print("Minimum Depth of the tree2 using iterative is:",min_depth_iterative(root))