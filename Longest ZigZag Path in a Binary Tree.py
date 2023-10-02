from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzag_helper(self, root, current, current_highest, was_left):
        current_highest[0] = max(current, current_highest[0])
        print(current)
        if root.left is not None:
            if was_left:
                self.zigzag_helper(root.left, 1, current_highest, True)
            else:
                self.zigzag_helper(root.left, current+1, current_highest, True)
        
        if root.right is not None:
            if was_left:
                self.zigzag_helper(root.right, current+1, current_highest, False)
            else:
                self.zigzag_helper(root.right, 1, current_highest, False)
        

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        current_highest = [0]
        if root.left is not None:
            self.zigzag_helper(root.left, 1, current_highest, True)
        if root.right is not None:
            self.zigzag_helper(root.right, 1, current_highest, False)
        return current_highest[0]

