# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned

        originalStack = [original]
        clonedStack = [cloned]

        while originalStack:
            node, clonedNode = originalStack.pop(), clonedStack.pop()
            if node == target:
                return clonedNode
            if node.left:
                originalStack.append(node.left)
                clonedStack.append(clonedNode.left)
            if node.right:
                originalStack.append(node.right)
                clonedStack.append(clonedNode.right)
