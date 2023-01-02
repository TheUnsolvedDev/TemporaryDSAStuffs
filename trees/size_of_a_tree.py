class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def size(root):
    queue = [root]
    count = 0
    while queue:
        root = queue.pop(0)
        if root:
            count += 1
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return count


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    print(size(root))
