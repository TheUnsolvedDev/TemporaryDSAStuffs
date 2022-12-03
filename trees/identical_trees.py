class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def check_identical(rootA, rootB):
    if rootA == None and rootB == None:
        return True
    if rootA and rootB:
        return (rootA.data == rootB.data) and check_identical(rootA.left, rootB.left) and check_identical(rootA.right, rootB.right)


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    root1 = node(1)
    root1.left = node(2)
    root1.right = node(3)
    root1.left.left = node(5)
    root1.left.right = node(4)
    root1.right.left = node(6)
    root1.right.right = node(7)

    print(check_identical(root, root1))
