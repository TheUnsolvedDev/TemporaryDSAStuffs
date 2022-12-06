class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.hd = 0


def top_view(root):
    queue = [root]
    hash_map = dict()

    while queue:
        root = queue.pop(0)
        hd = root.hd
        if hd not in hash_map:
            hash_map[root.hd] = root.data
        if root.left:
            queue.append(root.left)
            root.left.hd = hd - 1
        if root.right:
            queue.append(root.right)
            root.right.hd = hd + 1

    for i in sorted(hash_map.keys()):
        print(hash_map[i], end=' ')
    print(hash_map)


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    top_view(root)
