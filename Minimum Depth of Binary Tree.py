from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepthHelper(self, root, current, lowest):
        if root.left is not None:
            self.minDepthHelper(root.left, current+1, lowest)
        if root.right is not None:
            self.minDepthHelper(root.right, current+1, lowest)

        if root.left is None and root.right is None:
            lowest[0] = min(lowest[0], current)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        lowest = [float('inf')]
        if root is None:
            return 0
        self.minDepthHelper(root, 1, lowest)
        return lowest[0]