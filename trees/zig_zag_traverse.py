class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.hd = 0


def zig_zag_traversal(root):
    queue_curr_level = [root]
    queue_next_level = []
    left_to_right = True

    while queue_curr_level:
        root = queue_curr_level.pop(-1)
        print(root.data, " ", end="")
        if left_to_right:
            if root.left:
                queue_next_level.append(root.left)
            if root.right:
                queue_next_level.append(root.right)
        else:
            if root.right:
                queue_next_level.append(root.right)
            if root.left:
                queue_next_level.append(root.left)

        if len(queue_curr_level) == 0:
            left_to_right = not left_to_right
            queue_curr_level,queue_next_level = queue_next_level,queue_curr_level
    print()


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)
    
    zig_zag_traversal(root)
