class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_max(root, maxm=float('-inf')):
    if root is None:
        return maxm
    maxm = max(root.data, maxm)
    maxm = find_max(root.left, maxm)
    maxm = find_max(root.right, maxm)
    return maxm


def find_min(root, minm=float('inf')):
    if root is None:
        return minm
    minm = min(root.data, minm)
    minm = find_min(root.left, minm)
    minm = find_min(root.right, minm)
    return minm


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    print(find_max(root))
    print(find_min(root))
