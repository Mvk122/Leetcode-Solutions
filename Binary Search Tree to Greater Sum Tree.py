# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def helper(self, node, s):
        if node:
            self.helper(node.right, s)
            s[0] += node.val
            node.val = s[0]
            self.helper(node.left, s)
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = [0]
        self.helper(root, s)
        return root