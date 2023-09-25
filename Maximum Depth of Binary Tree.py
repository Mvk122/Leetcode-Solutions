from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        highest = [0]
        if root is None:
            return 0
        self.maxDepth_helper(root, 0, highest)
        return highest[0]

    def maxDepth_helper(self, node, current, highest):
        current += 1
        highest[0] = max(current, highest[0])
        if node.left is not None:
            self.maxDepth_helper(node.left, current, highest)
        if node.right is not None:
            self.maxDepth_helper(node.right, current, highest)
            