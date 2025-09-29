class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def find_parent(root, target, parent=None):
    if root is None:
        return None
    if root.data == target:
        return parent
    left_parent = find_parent(root.left, target, root)
    if left_parent is not None:
        return left_parent
    return find_parent(root.right, target, root)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    target = 5
    parent_node = find_parent(root, target)
    if parent_node:
        print(f"Parent of node {target} is: {parent_node.data}")
    else:
        print(f"Node {target} has no parent (it might be the root or not present in the tree).")

    target = 1
    parent_node = find_parent(root, target)
    if parent_node:
        print(f"Parent of node {target} is: {parent_node.data}")
    else:
        print(f"Node {target} has no parent (it might be the root or not present in the tree).")