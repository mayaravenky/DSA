class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def bfs_recursive(root,level,res):
    if root is None:
        return
    if len(res) == level:
        res.append([])

    res[level].append(root.data)
    bfs_recursive(root.left,level+1,res)
    bfs_recursive(root.right,level+1,res)
    return res
def bfs(root):
    res = []
    return bfs_recursive(root,0,res)

def bfs_iterative(root):
    if root is None:
        return []
    queue = []
    res = []
    queue.append(root)
    curr_level = 0
    while queue:
        len_level = len(queue)
        res.append([])
        for i in range(len_level):
            node = queue.pop(0)
            res[curr_level].append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        curr_level += 1
    return res

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print("BFS Traversal of the tree is:")
    print(bfs(root))
    print("BFS Iterative Traversal of the tree is:")
    print(bfs_iterative(root))