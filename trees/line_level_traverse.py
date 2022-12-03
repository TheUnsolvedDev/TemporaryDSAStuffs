class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def height(root):
    if root is None:
        return 0
    height_left = height(root.left)
    height_right = height(root.right)
    if height_left < height_right:
        return height_right + 1
    else:
        return height_left + 1


def childs(root, level=0):
    if root is None:
        return root
    if level == 1:
        print(root.data, end=' ')
    elif level > 1:
        childs(root.left, level-1)
        childs(root.right, level-1)


def line_level_traversal(root):
    height_of_tree = height(root)
    for i in range(height_of_tree):
        childs(root, i+1)
        print()


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    line_level_traversal(root)
    print()

    print(height(root))
