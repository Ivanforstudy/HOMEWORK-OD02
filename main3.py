class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

root = Node(50)

root = insert(root, 25)
root = insert(root, 75)
root = insert(root, 15)
root = insert(root, 35)
root = insert(root, 65)
root = insert(root, 85)