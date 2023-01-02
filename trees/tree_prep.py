class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root):
    if root != None:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')


def levelorder_traversal(root):
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        print(root.data, end=' ')
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

    preorder_traversal(root)
    print()
    inorder_traversal(root)
    print()
    postorder_traversal(root)
    print()
    levelorder_traversal(root)
    print()
